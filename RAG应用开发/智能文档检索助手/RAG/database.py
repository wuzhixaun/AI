from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean, ForeignKey,Index    
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from datetime import datetime
from sqlalchemy.dialects.mysql import MEDIUMTEXT



# 创建基类
Base = declarative_base()

# 文档模型
class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, autoincrement=True) # 文档id,自增,主键
    filename = Column(String(255), nullable=False) # 文档名称,不为空
    file_path = Column(String(500),nullable=False) # 文档路径,不为空
    content = Column(MEDIUMTEXT,nullable=False) # 文档内容,不为空
    chunk_count = Column(Integer,default=0) # 文档分块数量,不为空
    created_at = Column(DateTime,default=datetime.now) # 创建时间,不为空
    is_active = Column(Boolean,default=True) # 是否激活,不为空

    # 关联关系  设定一对多表   ParentChunk关联模型   back_populates 关联字段    cascade级联操作(删除操作)
    parent_chunks = relationship("ParentChunk", back_populates="document", cascade="all, delete-orphan")
    child_chunks = relationship("ChildChunk", back_populates="document", cascade="all, delete-orphan")

# 父文档
class ParentChunk(Base):
    __tablename__ = "parent_chunks"

    id = Column(Integer, primary_key=True, autoincrement=True) # 父文档id,自增,主键
    document_id = Column(Integer,ForeignKey("documents.id"),nullable=False) # 文档id,不为空
    parent_id = Column(String(100), nullable=False, unique=True)  # 父文档唯一标识
    content = Column(Text,nullable=False) # 父文档内容,不为空
    json_metadata = Column(Text)  # JSON格式存储元数据
    vector_id = Column(String(100))  # Chroma中的向量ID
    created_at = Column(DateTime,default=datetime.now) # 创建时间,不为空

    # 关联关系
    document = relationship("Document", back_populates="parent_chunks") # 关联文档模型
    child_chunks = relationship("ChildChunk", back_populates="parent_chunk", cascade="all, delete-orphan")

    # 创建索引
    __table_args__ = (
        Index("idx_parent_document_id", "document_id"),
        Index("idx_parent_id", "parent_id"),
    )


# 子文档
class ChildChunk(Base):
    __tablename__ = "child_chunks"

    id = Column(Integer, primary_key=True, autoincrement=True) # 子文档id,自增,主键
    document_id = Column(Integer,ForeignKey("documents.id"),nullable=False) # 文档id,不为空
    parent_chunk_id = Column(String(100),ForeignKey("parent_chunks.id"),nullable=False) # 父文档id,不为空
    child_id = Column(String(100), nullable=False)  # 子文档唯一标识
    content = Column(Text,nullable=False) # 子文档内容,不为空
    json_metadata = Column(Text)  # JSON格式存储元数据
    vector_id = Column(String(100))  # Chroma中的向量ID
    created_at = Column(DateTime,default=datetime.now) # 创建时间,不为空

    # 关联关系
    document = relationship("Document", back_populates="child_chunks")
    parent_chunk = relationship("ParentChunk", back_populates="child_chunks")

    # 创建索引
    __table_args__ = (
        Index('idx_child_document_id', 'document_id'),
        Index('idx_child_parent_id', 'parent_chunk_id'),
        Index('idx_child_id', 'child_id'),
    )


# 聊天历史
class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(100), nullable=False) # 会话id,不为空
    user_message = Column(Text,nullable=False) # 用户消息,不为空
    assistant_message = Column(Text,nullable=False) # 助手消息,不为空
    document_ids = Column(500) # 相关文档id,不为空
    used_chunks = Column(500) # 使用过的子文档id,不为空
    created_at = Column(DateTime,default=datetime.now) # 创建时间,不为空

    # 创建索引
    __table_args__ = (
        Index('idx_chat_session_id', 'session_id'),
        Index('idx_chat_created_at', 'created_at'),
    )


# 数据库管理类
class DatabaseManager:
    
    def __init__(self, config):
        """初始化数据库管理类"""
        self.config = config
        self.engine = None
        self.SessionLocal = None
        self.init_database()

    
    def init_database(self):
        """初始化数据库"""
        # 创建数据库连接
        connection_string = f"mysql+pymysql://{self.config['MYSQL_USER']}:{self.config['MYSQL_PASSWORD']}@{self.config['MYSQL_HOST']}:{self.config['MYSQL_PORT']}/{self.config['MYSQL_DATABASE']}?charset=utf8mb4"
        
        try:
            self.engine = create_engine(connection_string,echo=True)
            # 创建所有的标配
            Base.metadata.create_all(self.engine)
            self.SessionLocal = sessionmaker(bind=self.engine)
            print("数据库连接成功")

        except Exception as e:
            print(f"Error initializing database: {e}")
            raise e
    

    def get_session(self):
        """获取会话"""
        return self.SessionLocal()

    # 保存文档及其子文档
    def save_document_with_chunks(self, filename, file_path, content, parent_docs, child_docs, parent_vector_id, child_vector_id):
        """保存文档及其子文档"""

        # 获取数据库会话
        session = self.get_session()

        try:
            # 保存主文档
            document = Document(filename=filename, file_path=file_path, content=content, chunk_count = len(child_docs))
            session.add(document)
            session.flush()

            doc_id = document.id

            # 保存父文档
            parent_chunk_map = {}  # parent_id -> parent_chunk_id 映射
            for i, (parent_doc, vector_id) in enumerate(zip(parent_docs,parent_vector_id)):
                parent_chunk = ParentChunk(document_id=document.id, parent_id=parent_doc.metadata.get('parent_id', f'parent_{i}'), content=parent_doc.page_content, json_metadata = str(parent_doc.metadata), vector_id=vector_id)
                session.add(parent_chunk)
                session.flush()

                parent_chunk_map[parent_chunk.parent_id] = parent_chunk.id

            # 保存子文档
            for child_doc,vector_id in zip(child_docs,child_vector_id):
                parent_id = child_doc.metadata.get('parent_id', 'unknown')
                parent_chunk_id = parent_chunk_map.get(parent_id)

                child_chunk = ChildChunk(
                    document_id=doc_id,
                    parent_chunk_id=parent_chunk_id,
                    child_id=child_doc.metadata.get('child_id', f'child_{len(child_docs)}'),
                    content=child_doc.page_content,
                    json_metadata=str(child_doc.metadata),
                    vector_id=vector_id
                )
                session.add(child_chunk)

            session.commit()
            print(f"Document and chunks saved successfully: {filename}")
            return doc_id

        except Exception as e:
            print(f"Error saving document with chunks: {e}")
            raise e
        
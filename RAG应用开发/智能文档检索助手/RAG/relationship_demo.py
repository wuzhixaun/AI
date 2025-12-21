"""
relationship 使用示例
这个文件展示了如何使用 SQLAlchemy 的 relationship 来访问关联数据
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Document, ParentChunk, ChildChunk
from config import Config
from datetime import datetime

# 创建数据库连接
DATABASE_URL = f"mysql+pymysql://{Config.MYSQL_USER}:{Config.MYSQL_PASSWORD}@{Config.MYSQL_HOST}:{Config.MYSQL_PORT}/{Config.MYSQL_DATABASE}"
engine = create_engine(DATABASE_URL)

# 创建会话工厂
SessionLocal = sessionmaker(bind=engine)

# 创建数据库表（如果不存在）
Base.metadata.create_all(engine)


def demo_relationship_usage():
    """演示 relationship 的各种使用方法"""
    
    # 创建数据库会话
    session = SessionLocal()
    
    try:
        print("=" * 60)
        print("relationship 使用示例")
        print("=" * 60)
        
        # ========== 示例1: 通过文档访问所有父块 ==========
        print("\n【示例1】通过文档访问所有父块")
        print("-" * 60)
        
        # 查询一个文档
        doc = session.query(Document).first()
        
        if doc:
            print(f"文档名称: {doc.filename}")
            print(f"文档ID: {doc.id}")
            
            # 使用 relationship 访问该文档的所有父块
            # 注意：这里直接使用 doc.parent_chunks，不需要写 JOIN 查询！
            parent_chunks = doc.parent_chunks
            print(f"该文档有 {len(parent_chunks)} 个父块:")
            
            for chunk in parent_chunks:
                print(f"  - 父块ID: {chunk.parent_id}, 内容预览: {chunk.content[:50]}...")
        else:
            print("数据库中没有文档，请先创建一些数据")
        
        # ========== 示例2: 通过父块访问所属文档 ==========
        print("\n【示例2】通过父块访问所属文档")
        print("-" * 60)
        
        # 查询一个父块
        parent_chunk = session.query(ParentChunk).first()
        
        if parent_chunk:
            print(f"父块ID: {parent_chunk.parent_id}")
            print(f"父块内容预览: {parent_chunk.content[:50]}...")
            
            # 使用 relationship 访问该父块所属的文档
            # 注意：这里直接使用 parent_chunk.document，不需要写 JOIN 查询！
            doc = parent_chunk.document
            print(f"所属文档: {doc.filename}")
            print(f"文档ID: {doc.id}")
        else:
            print("数据库中没有父块")
        
        # ========== 示例3: 通过文档访问所有子块 ==========
        print("\n【示例3】通过文档访问所有子块")
        print("-" * 60)
        
        if doc:
            # 使用 relationship 访问该文档的所有子块
            child_chunks = doc.child_chunks
            print(f"文档 '{doc.filename}' 有 {len(child_chunks)} 个子块:")
            
            for chunk in child_chunks:
                print(f"  - 子块ID: {chunk.child_id}, 内容预览: {chunk.content[:50]}...")
        
        # ========== 示例4: 通过父块访问所有子块 ==========
        print("\n【示例4】通过父块访问所有子块")
        print("-" * 60)
        
        if parent_chunk:
            # 使用 relationship 访问该父块的所有子块
            child_chunks = parent_chunk.child_chunks
            print(f"父块 '{parent_chunk.parent_id}' 有 {len(child_chunks)} 个子块:")
            
            for chunk in child_chunks:
                print(f"  - 子块ID: {chunk.child_id}, 内容预览: {chunk.content[:50]}...")
        
        # ========== 示例5: 通过子块访问父块和文档 ==========
        print("\n【示例5】通过子块访问父块和文档")
        print("-" * 60)
        
        child_chunk = session.query(ChildChunk).first()
        
        if child_chunk:
            print(f"子块ID: {child_chunk.child_id}")
            print(f"子块内容预览: {child_chunk.content[:50]}...")
            
            # 访问所属的父块
            parent = child_chunk.parent_chunk
            print(f"所属父块ID: {parent.parent_id}")
            
            # 访问所属的文档
            doc = child_chunk.document
            print(f"所属文档: {doc.filename}")
        
        # ========== 示例6: 创建关联数据 ==========
        print("\n【示例6】创建关联数据")
        print("-" * 60)
        
        # 创建一个新文档
        new_doc = Document(
            filename="示例文档.txt",
            file_path="/path/to/示例文档.txt",
            content="这是一个示例文档的内容...",
            chunk_count=0
        )
        session.add(new_doc)
        session.flush()  # 获取文档ID
        
        # 创建父块，直接关联到文档对象（不需要手动设置 document_id）
        new_parent_chunk = ParentChunk(
            parent_id="parent_001",
            content="这是父块的内容...",
            document=new_doc  # 直接赋值文档对象，SQLAlchemy 会自动设置 document_id
        )
        session.add(new_parent_chunk)
        session.flush()
        
        # 创建子块，关联到文档和父块
        new_child_chunk = ChildChunk(
            child_id="child_001",
            content="这是子块的内容...",
            document=new_doc,  # 直接赋值文档对象
            parent_chunk=new_parent_chunk  # 直接赋值父块对象
        )
        session.add(new_child_chunk)
        
        # 提交事务
        session.commit()
        print("✓ 成功创建关联数据")
        
        # ========== 示例7: 级联删除 ==========
        print("\n【示例7】级联删除（删除文档时自动删除关联的块）")
        print("-" * 60)
        
        # 由于设置了 cascade="all, delete-orphan"
        # 删除文档时，会自动删除所有关联的父块和子块
        test_doc = session.query(Document).filter(Document.filename == "示例文档.txt").first()
        if test_doc:
            print(f"删除文档: {test_doc.filename}")
            print(f"删除前，该文档有 {len(test_doc.parent_chunks)} 个父块")
            session.delete(test_doc)
            session.commit()
            print("✓ 文档已删除，关联的父块和子块也会自动删除")
        
        print("\n" + "=" * 60)
        print("所有示例演示完成！")
        print("=" * 60)
        
    except Exception as e:
        print(f"发生错误: {e}")
        session.rollback()
    finally:
        session.close()


def demo_without_relationship():
    """对比：不使用 relationship 的复杂查询方式"""
    
    session = SessionLocal()
    
    try:
        print("\n" + "=" * 60)
        print("对比：不使用 relationship 的复杂方式")
        print("=" * 60)
        
        # 不使用 relationship，需要手动写 JOIN 查询
        from sqlalchemy.orm import joinedload
        
        doc = session.query(Document).options(
            joinedload(Document.parent_chunks)
        ).first()
        
        if doc:
            print(f"文档: {doc.filename}")
            # 即使使用了 joinedload，访问方式还是一样的
            print(f"父块数量: {len(doc.parent_chunks)}")
        
        # 或者使用原生 SQL JOIN
        result = session.execute("""
            SELECT d.*, p.* 
            FROM documents d 
            LEFT JOIN parent_chunks p ON d.id = p.document_id 
            WHERE d.id = 1
        """)
        
        print("\n使用 relationship 的优势：")
        print("1. 代码更简洁，不需要写复杂的 JOIN 查询")
        print("2. 可以直接通过对象属性访问关联数据")
        print("3. 支持级联操作（自动删除关联数据）")
        print("4. 更符合面向对象编程思想")
        
    finally:
        session.close()


if __name__ == "__main__":
    # 运行示例
    demo_relationship_usage()
    
    # 运行对比示例
    demo_without_relationship()




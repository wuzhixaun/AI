from langchain_text_splitters import RecursiveCharacterTextSplitter
import logging
import tempfile
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
import os
logger = logging.getLogger("simple_logger")


class DocumentProcessor:
    def __init__(self, config):
        self.config = config

        # 主文档分割器
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE, 
            chunk_overlap=config.CHUNK_OVERLAP,
            separators=["\n\n", "\n", "。", "！", "？", ".", "!", "?", " ", ""]
        )

        # 创建父文档分割器
        self.parent_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE * 2,
            chunk_overlap=config.CHUNK_OVERLAP ,
            separators=["\n\n", "\n", "。", "！", "？"]
        )

        # 创建子文档分割器
        self.child_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE // 2 ,
            chunk_overlap=config.CHUNK_OVERLAP // 2,
            separators=["\n", "。", "！", "？", ".", "!", "?", " "]
        )

    def load_document(self, uploaded_file):
        """加载文档"""
        # 判断文件的类型
        # 保存临时文件
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name
        print(tmp_path)

        try:
            # 根据文件类型选择不同的加载器
            if uploaded_file.type == "application/pdf":
                loader = PyPDFLoader(tmp_path)
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                loader = Docx2txtLoader(tmp_path)
            elif uploaded_file.type == "text/plain":
                loader = TextLoader(tmp_path)
            else:
                logger.error("document_processor load_document unsupported file type: %s", uploaded_file.type)

            # 加载文档
            documents = loader.load()
            return documents
        except Exception as e:
            logger.error("document_processor load_document error: %s", e)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
    
    def create_parent_child_chunks(self, documents, fileNmae):
        """创建父文档和子文档"""
       
        try:
           parent_docs = self.parent_splitter.split_documents(documents)
           child_docs = []
           for i, parent_doc in enumerate(parent_docs):
                # 为每个父文档生成一个 id
                parent_id = f"{fileNmae}_parent_{i}"
                parent_doc.metadata['parent_id'] = parent_id
                parent_doc.metadata['doc_type'] = 'parent'

                # 从父文档创建子文档
                child_chunks = self.child_splitter.split_documents([parent_doc])

                for j, child_doc in enumerate(child_chunks):
                    child_id = f"{fileNmae}_child_{i}_{j}"
                    child_doc.metadata['child_id'] = child_id
                    child_doc.metadata['doc_type'] = 'child'
                    child_doc.metadata['parent_id'] = parent_id
                    child_docs.append(child_doc)
                    
           return parent_docs, child_docs

        except Exception as e:
            logger.error("document_processor create_parent_child_chunks error: %s", e)
            return None, None
from langchain_huggingface import HuggingFaceEmbeddings
import chromadb
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
import logging
from langchain_classic.retrievers import ContextualCompressionRetriever
logger = logging.getLogger(__name__)


class VectorStore:
    def __init__(self, config):
        self.config = config
        # 本地向量模型路径
        self.LOCAL_MODEL_PATH = config.LOCAL_MODEL_PATH

        # 初始化向量模型
        self.embeddings = HuggingFaceEmbeddings(model_name=self.LOCAL_MODEL_PATH)

        # 初始化Chroma客户端
        self.chroma_client = chromadb.PersistentClient(path=self.config.CHROMA_PERSIST_DIR)

        # 父文档和子文档使用不同的集合
        self.parent_vector_store = Chroma(
            collection_name="parent_chunks",
            client=self.chroma_client,
            embedding_function=self.embeddings
        )

        self.child_vector_store = Chroma(
            collection_name="child_chunks",
            client=self.chroma_client,
            embedding_function=self.embeddings
        )

        # 初始化上下文压缩器
        self.llm = ChatOpenAI(
            api_key=config.OPENAI_API_KEY,
            base_url=config.OPENAI_BASE_URL,
            model="qwen-plus",
            temperature=0
        )
        
        self.compressor = LLMChainExtractor.from_llm(self.llm)

    
    def add_documents(self, parent_docs, child_docs, document_id):
        """添加文档"""
        try:
            # 为所有文档添加document_id元数据
            for doc in parent_docs + child_docs:
                doc.metadata['document_id'] = document_id

            # 添加父文档
            parent_ids = self.parent_vector_store.add_documents(parent_docs)
            # 添加子文档
            child_ids = self.child_vector_store.add_documents(child_docs)
            
            return parent_ids, child_ids
        except Exception as e:
            logger.error("vector_store add_documents error: %s", e)
            raise e

    def create_retriever(self, use_compression=True):
        """创建检索器"""

        try:
            child_retriever = self.child_vector_store.as_retriever(search_kwargs={
                "k": self.config.TOP_K * 2,  # 获取更多子文档
            })

            if use_compression:
                # 使用上下文压缩检索器
                compression_retriever = ContextualCompressionRetriever(
                base_compressor=self.compressor,
                base_retriever=child_retriever
                )
                return compression_retriever
            
            else:
                return child_retriever  



        except Exception as e:
            print(f"create_child_retriever error: {e}")
            raise e

        

    def get_parent_documents(self, child_docs):
        """根据子文档获取对应的父文档"""

        try:
            parent_ids = set()
            for doc in child_docs:
                if 'parent_id' in doc.metadata:
                    parent_ids.add(doc.metadata['parent_id'])
            return self.get_parent_documents_by_metadata(list(parent_ids))

        except Exception as e:
            print(f"get_parent_documents error: {e}")
            raise e


    def get_parent_documents_by_metadata(self, parent_ids):
        """根据parent_id列表获取父文档"""

        if not parent_ids:
            return []
        
        parent_docs = []
        
        for parent_id in parent_ids:
            try:
                # 使用相似度搜索并过滤parent_id
                results = self.parent_vector_store.get(where={"parent_id": parent_id})
                parent_docs.extend(results['documents'][0])  # 每个parent_id只取一个结果
            except Exception as e:
                print(f"获取父文档时出错 (parent_id: {parent_id}): {e}")
                continue
        
        return parent_docs
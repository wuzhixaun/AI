import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_chroma import Chroma

# 加载环境变量
load_dotenv()

# 获取环境变量
embedding_model_path = os.getenv("EMBEDDING_MODEL")

# 初始化嵌入模型
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_path)

# 创建文档加载器
loader = UnstructuredWordDocumentLoader("人事管理流程.docx")

# 加载文档
docs = loader.load()

# 创建文档分割器
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30)

# 分割文档
chunks = text_splitter.split_documents(docs)

# 创建向量数据库
# 注意：LangChain 会自动创建和管理 collection，无需手动创建
# 如果不指定 collection_name，LangChain 会使用默认名称
# 如果需要多个独立的集合，可以指定 collection_name 参数
vector_db = Chroma(
    embedding_function=embeddings,
    persist_directory="vector_learn.db"
    # collection_name="my_documents",  # 可选：显式指定 collection 名称
    # client=None,  # 可选：传入已创建的 ChromaDB 客户端
)

# 添加文档
# vector_db.add_documents(chunks)

# 查询文档
docs = vector_db.similarity_search("请假流程",k=2)
print(docs)

# 删除文档
vector_db.delete(ids=["1"])

# 查询文档
# docs = vector_db.similarity_search("请假流程",k=2)
vector_db.query(query_texts=["请假流程"],n_results=2)
print(docs)
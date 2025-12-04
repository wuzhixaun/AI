import os

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import WebBaseLoader,UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 加载环境变量
load_dotenv()

# 本地embedding模型地址
embedding_model_path = os.getenv("EMBEDDING_MODEL")

# 初始化嵌入模型（用于文本向量化）
embeddings_model = HuggingFaceEmbeddings(model_name=embedding_model_path)

url = "https://news.pku.edu.cn/mtbdnew/15ac0b3e79244efa88b03a570cbcbcaa.htm"


# 初始化文档加载器列表（加载多个文本文件）
loaders = [WebBaseLoader(url), UnstructuredWordDocumentLoader("人事管理流程.docx")]

# 加载文档
docs = [loader.load() for loader in loaders]

# 初始化文档分割器
text_splitter = RecursiveCharacterTextSplitter(chunk_size= 1024,chunk_overlap=100)

docs = text_splitter.split_documents(docs)
print(docs)
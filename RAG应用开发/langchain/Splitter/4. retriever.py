from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
import os
from dotenv import load_dotenv


# 加载环境变量
load_dotenv()

# 创建pdf加载器
loader = PyPDFLoader(r"/Users/wuzhixuan/code/project/AI/财务管理文档.pdf")

# 加载文档
pages = loader.load_and_split()

# 创建DashScopeEmbeddings
embeddings_model = DashScopeEmbeddings(
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
    model="text-embedding-v4",
)

# 创建分割器
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=100,length_function=len)

# 将数据进行切割成块
paragraphs = text_splitter.create_documents([page.page_content for page in pages])

# 创建chroma数据库，并将文本数据个向量化的数据存入
db = Chroma.from_documents(paragraphs, embeddings_model)

# 实例化 retriever
retriever = db.as_retriever()

# 限制返回的文档数量
# retriever = db.as_retriever(search_kwargs={"k": 2})

# 获取相关文档
docs = retriever.invoke("会计核算基础规范")
for doc in docs:
    print(doc.page_content)
    print("-"*100)
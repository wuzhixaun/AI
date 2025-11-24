import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Document loaders
from langchain_community.document_loaders import WebBaseLoader

# Embeddings
from langchain_community.embeddings import DashScopeEmbeddings

# Vector DB
from langchain_vector_store import faiss_conn
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Retrieval Chains (新版)
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# 加载环境变量
load_dotenv()

# 创建提示词模版
prompt = ChatPromptTemplate.from_template("""仅根据提供的上下文回答以下问题:

<context>
{context}
</context>

问题: {input}""")


# 创建llm连接
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"),model="qwen-plus")

# 创建文档组合链  将文档内容和用户问题组合成一个完整的提示，然后传递给语言模型生成回答
document_chain = create_stuff_documents_chain(llm, prompt)

# 生成检索器示例
retriever = faiss_conn().as_retriever()

retriever.search_kwargs = {"k": 3}  # 限制为最多检索3个文档

# 创建检索链   该链结合了检索器和文档组合链，实现了从向量数据库中检索相关文档，并将这些文档与用户问题组合成提示
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# 调用检索链并获取回答
response = retrieval_chain.invoke({"input": "条例是什么时候开始执行，第几条准则规定的"})

print(response["answer"])
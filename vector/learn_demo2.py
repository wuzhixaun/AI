import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai.llms import base
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI

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
vector_db.add_documents(chunks)

# 创建提示词

prompt = PromptTemplate(
            template="""
            你是一个智能助手。请基于以下上下文信息回答用户的问题。如果上下文中没有相关信息，请诚实地说明。

            上下文信息：
            {context}


            用户问题:
            {question}

            请提供准确、有帮助的回答:
            """,
            input_variables=["context", "question"]
        )

# 创建检索器
retriever = vector_db.as_retriever(search_kwargs={"k": 5})

# 查询相关文档
question = "请假流程是什么"

retrieved_docs = retriever.invoke(question)



# 将 Document 列表拼接为纯文本上下文
context = "\n".join(doc.page_content for doc in retrieved_docs)
print("最终检索的上下文：", retrieved_docs)


# 构建完整提示
full_prompt = prompt.format(
context=context,
question=question
)

print("full_prompt",full_prompt)

# 创建 llm
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url= os.getenv("DASHSCOPE_BASE_URL"),model=os.getenv("LLM_MODEL"))

# 调用大模型
answer = llm.invoke(full_prompt).content
print("答案=",answer)
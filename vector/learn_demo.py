import os 
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage, content
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

# 加载环境变量
load_dotenv()

# 获取环境变量
embedding_model_path = os.getenv("EMBEDDING_MODEL")

# 初始化嵌入模型
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_path)


long_text = """
人工智能（Artificial Intelligence，AI）是计算机科学的一个分支，致力于创建能够执行通常需要人类智能的任务的系统。
这些任务包括学习、推理、问题解决、感知和语言理解。

机器学习是人工智能的一个子集，它使计算机能够在没有被明确编程的情况下学习和改进。
深度学习是机器学习的一个子集，使用人工神经网络来模拟人脑的工作方式。

自然语言处理（NLP）是AI的另一个重要分支，专注于计算机与人类语言之间的交互。
这包括文本理解、语言生成、机器翻译和情感分析等任务。

计算机视觉使机器能够从数字图像或视频中获取有意义的信息。
它包括图像识别、物体检测、人脸识别和图像生成等技术。
"""

# 文档分割器
text_splitter = RecursiveCharacterTextSplitter(chunk_size=30, chunk_overlap=10)

# 分割文档
chunks = text_splitter.split_text(long_text)

# 创建向量数据库
vector_db = Chroma(
    collection_name="vector_learn2",
    embedding_function=embeddings,
    persist_directory="vector_learn2.db"
)

# 3. 准备数据
datas = [
    "苹果是一种水果，富含维生素",
    "Python是一种编程语言",
    "机器学习算法可以预测未来趋势",
    "香蕉含有丰富的钾元素",
    "深度学习是机器学习的子集"
]
ids = [f"doc_{i}" for i in range(len(datas))]

docs = vector_db.similarity_search("苹果",k=1)
# print(docs)

# 删除向量doc_1
vector_db.delete(ids = ['doc_1'])


# 查询所有的文档
retriever = vector_db.as_retriever(search_kwargs={"k": 3})
mydocs = retriever.invoke("苹果")

# 创建 OpenAI
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"),model=os.getenv("LLM_MODEL"))

# 1) 最简单：字符串模板 -> 一次性格式化
# tpl = PromptTemplate.from_template("用一句话解释：{topic}")
# prompt_str = tpl.format(topic="机器学习")  # 得到纯字符串

# print("-"*100)
# print(tpl)
# print("-"*100)
# print(prompt_str)
# print("-"*100)
# result = llm.invoke(prompt_str)
# print(result)


# 2) ChatPromptTemplate：多消息，适合聊天模型
chat_prompt = ChatPromptTemplate.from_messages([("system", "你是专业技术助手，回答要简洁"),("human","请解释 {topic}")])


msg_list = chat_prompt.format_messages(topic="向量数据库")  # 得到消息列表

result = llm.invoke(msg_list)  # 直接喂给 chat 模型
print(chat_prompt)
print("-"*100)
print(msg_list)
print("-"*100)
print(result)
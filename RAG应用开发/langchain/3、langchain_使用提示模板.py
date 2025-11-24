import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 加载环境变量
load_dotenv()

# 创建 langchain client
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"),model="qwen-plus")

# 创建提示模板
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "您是世界级的技术文档编写者"),
        ("user","{input}")
    ]
)


# 调用 llm
chain = prompt | llm

response = chain.invoke({"input":"请编写一份关于大模型的技术文档,字数 200 以内"})

print(response.content)
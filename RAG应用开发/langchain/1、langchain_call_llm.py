from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# 加载环境变量
load_dotenv()

# 创建 langchain client
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"),model="qwen-plus")

# 调用 llm
response = llm.invoke("什么是大模型?")

print("="*70)
print(response)

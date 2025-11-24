import os 
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os 

# 加载环境变量
load_dotenv()

# 创建OpenAI客户端
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"),model="qwen-plus")

# 创建提示词模版
human_text = "你好啊"
system_text = "你是一个强大的助手，你的名字叫0713"

# messages = [HumanMessage(content=human_text)]
# 聊天模型支持多个消息作为输入
messages = [SystemMessage(content=system_text), HumanMessage(content=human_text)]

res = llm.invoke(messages)
print(res.content)
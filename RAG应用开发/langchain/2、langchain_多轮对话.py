from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage, HumanMessage, AIMessage

# 加载环境变量
load_dotenv()

# 创建 langchain client
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"),model="qwen-plus")

# 创建系统消息
messages = [
    SystemMessage(content="你是各位老师的个人助理。你叫小戈"), # 等价于OpenAI接口中的system role 系统消息
    HumanMessage(content="我的名字叫小吴"), # 等价于OpenAI接口中的user role 用户输入的消息
    AIMessage(content="不好意思，暂时无法获取天气情况"), # 等价于OpenAI接口中的assistant role AI 模型的回复消息
    HumanMessage(content="查询南昌的交通情况")
]

# 调用 llm
response = llm.invoke(messages)

print("="*70)
print(response.content)
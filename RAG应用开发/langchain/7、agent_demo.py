from langchain_openai import ChatOpenAI
from langsmith import Client as LangSmithClient
from langchain_classic.agents import create_openai_functions_agent, AgentExecutor  # 使用 langchain-classic 中的旧 API
from langchain_core.tools import create_retriever_tool
import os
from dotenv import load_dotenv
from langchain_vector_store import faiss_conn
from openai import OpenAI

# 加载环境变量
load_dotenv()

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# 创建OpenAI客户端
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"),model="qwen-plus")

# 创建检索器
retriever = faiss_conn().as_retriever()

# 创建工具
retriever_tool = create_retriever_tool(retriever, name="生态环境监测条例的一个检索器工具", description="搜索生态环境监测条例的工具，关于生态环境监测条例的任何问题，都可以使用这个工具进行搜索")

# 创建工具列表
tools = [retriever_tool]

langsmith_client = LangSmithClient(api_key=os.getenv("LANGSMITH_API_KEY"))

# 创建提示词（从 langchain-hub 获取）
prompt = langsmith_client.pull_prompt("hwchase17/openai-functions-agent")

print(prompt)

# 创建代理（使用 langchain-classic 中的旧 API）
agent = create_openai_functions_agent(llm, tools, prompt)

# 创建代理执行器,verbose=True 表示输出详细信息
agent_executor = AgentExecutor(agent=agent, tools=tools,verbose=True,handle_parsing_errors=True)

# 执行代理
response = agent_executor.invoke({"input": "生态环境监测条例第三十条是什么？"})

print(response)





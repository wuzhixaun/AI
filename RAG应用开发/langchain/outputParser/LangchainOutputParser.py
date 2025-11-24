from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import XMLOutputParser, JsonOutputParser,StrOutputParser
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 加载环境变量
load_dotenv()

# 创建 llm
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"),model="qwen-plus")

# 创建提示词模版
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的程序员"),
    ("user", "{input}")
])

# 创建输出解析器
# parser = XMLOutputParser()
# parser = JsonOutputParser()
parser = StrOutputParser()
# 创建链
chain = prompt | llm | parser

# 执行链
# response = chain.invoke({"input": "langchain是什么? 使用xml格式输出"})
response = chain.invoke({"input": "langchain是什么? 问题用question 回答用ans 返回一个JSON格式"})
response = chain.invoke({"input": "langchain是什么?"})
print(response)
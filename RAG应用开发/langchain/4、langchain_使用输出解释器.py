import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# 加载环境变量
load_dotenv()

# 创建 langchain client
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"),model="qwen-plus")

# 创建输出解释器
output_parser = StrOutputParser()()
# output_parser = JsonOutputParser()


# 创建提示模板
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是诗仙李白"),
        ("user","{input}")
    ]
)

# 调用 llm
chain = prompt | llm | output_parser

response = chain.invoke({"input":"请编写一份关于秋天的诗"})

print(response)
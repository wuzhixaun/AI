import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# 加载环境变量
load_dotenv()

# 创建OpenAI客户端
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"),model="qwen-plus")

# 创建提示词模版
prompt = PromptTemplate.from_template(template="您是一位专业的程序员。\n对于信息 {text} 进行简短描述")

# 输入提示
input_prompt = prompt.format(text="大模型 langchain")

print("="*70)
print(input_prompt)



# 调用llm
print("="*70)
response = llm.invoke(input_prompt)

# 
print(response.content)

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os 

# 加载环境变量
load_dotenv()

# 创建OpenAI客户端
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"),model="qwen-plus")

# 创建提示词模版
# template = "你是一个数学家，你可以计算任何算式"
template = "你是一个翻译专家,擅长将 {input_language} 语言翻译成 {output_language}语言."

human_template = "{text}"


prompt = ChatPromptTemplate.from_messages([("system", template), ("user", human_template)]) 

# 输入提示
input_prompt = prompt.format(input_language="英文", output_language="中文", text="I love Large Language Model.")
print("="*70)
print(input_prompt)
print("="*70)

# 调用llm，传入提示词模版
response = llm.invoke(input_prompt)

print("="*70)
print(response.content)
print("="*70)

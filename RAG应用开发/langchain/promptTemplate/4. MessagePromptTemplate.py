import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate)
import os 

# 加载环境变量
load_dotenv()

# 创建OpenAI客户端
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"),model="qwen-plus")

# 创建提示词模版
system_message_prompt = SystemMessagePromptTemplate.from_template("你是一个翻译专家,擅长将 {input_language} 语言翻译成 {output_language}语言.")
human_message_prompt = HumanMessagePromptTemplate.from_template("{text}")

# 组装成最终模版
chatPromptTemplate = ChatPromptTemplate.from_messages([system_message_prompt,human_message_prompt])

# 输入提格式化提示消息生成提示示
input_prompt = chatPromptTemplate.format(input_language="英文", output_language="中文", text="I love Large Language Model.")

# 打印提示词
print("="*70)
print(input_prompt)
print("="*70)

# 调用llm，传入提示词模版
response = llm.invoke(input_prompt)

print("="*70)
print(response.content)
print("="*70)
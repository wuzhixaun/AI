# @author wuzhixuan
# @date 2025-01-27

"""
StringPromptTemplate 使用示例

说明：
- StringPromptTemplate 是抽象基类，不能直接实例化
- 应该使用 PromptTemplate（它是 StringPromptTemplate 的具体实现）
- PromptTemplate 用于创建字符串格式的提示词模板
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate  # 使用 PromptTemplate（StringPromptTemplate 是抽象基类）
from langchain_core.messages import HumanMessage

# 加载环境变量
load_dotenv()

# 创建OpenAI客户端
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"),model="qwen-plus")

# 创建提示词模版（PromptTemplate 是 StringPromptTemplate 的具体实现）
prompt_template = PromptTemplate(
    template="您是一位专业的程序员。\n对于信息 {text} 进行简短描述",
    input_variables=["text"]  # 指定模板中的变量
)

# 格式化提示词（传入变量值）
prompt = prompt_template.format(text="大模型 langchain")

print("="*70)
print("格式化后的提示词：")
print(prompt)
print("="*70)

# 调用llm（ChatOpenAI 需要消息对象）
# 方法1：使用 format_prompt 返回 PromptValue，然后转换为消息
prompt_value = prompt_template.format_prompt(text="大模型 langchain")
# response = llm.invoke([HumanMessage(content=prompt_value.to_string())])

# 或者方法2：直接使用格式化后的字符串
response = llm.invoke(prompt)

print("="*70)
print("LLM 回复：")
print(response.content)
print("="*70)
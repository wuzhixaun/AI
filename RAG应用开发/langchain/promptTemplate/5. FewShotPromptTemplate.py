import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
import langchain_openai
load_dotenv()
# 创建示例
examples = [
    {"input": "2+2", "output": "4", "description": "加法运算"},
    {"input": "5-2", "output": "3", "description": "减法运算"},
]
prompt_template = "你是一个数学专家,算式： {input} 值： {output} 使用： {description} "

# 这是一个提示模板，用于设置每个示例的格式
prompt_sample = PromptTemplate.from_template(prompt_template)

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=prompt_sample,
    # 告诉大模型要按照这个格式输出description
    suffix="""你是一个数学专家,请计算： {input} 值： {output} """,
    input_variables=["input", "output"],
)

# 创建 llm
llm = langchain_openai.ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"),model="qwen-plus")

# 创建提示词模版
prompt = prompt.format(input="2*5", output="10")

# 打印提示词
print("="*70)
print(prompt)
print("="*70)

# 调用llm，传入提示词模版
response = llm.invoke(prompt)

print("="*70)
print(response.content)
print("="*70)
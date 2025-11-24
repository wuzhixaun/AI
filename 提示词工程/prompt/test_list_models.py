from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # 从我们的env⽂件中加载出对应的环境变量

# 创建OpenAI客户端
client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"))

models = client.models.list()

# 打印模型列表
print(models.data)

# 打印模型列表
for i in models.data:
    print(i.id)
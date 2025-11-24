from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # 从我们的env⽂件中加载出对应的环境变量

# 创建OpenAI客户端
client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"))


def get_embedding(text):
    """
    获取文本的向量嵌入
    """
    response = client.embeddings.create(
        input=text,
        model="text-embedding-v4"
    )
    return response.data[0].embedding


    
query_text = ['我爱你']

# 打印向量嵌入

embedding = get_embedding(query_text)
print(embedding)

print(len(embedding))
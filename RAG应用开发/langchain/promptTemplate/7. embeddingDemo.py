import os 
from langchain_community.embeddings import DashScopeEmbeddings
from dotenv import load_dotenv


# 加载环境变量
load_dotenv()

# 创建DashScopeEmbeddings
embeddings = DashScopeEmbeddings(dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),model="text-embedding-v4")

# 获取文本嵌入向量
text = '大模型'

# 嵌入文档 把文档内容转换为向量 他支持多个文档列表形式
doc_res = embeddings.embed_documents([text])


# 嵌入查询
query_res = embeddings.embed_query(text)

print("-"*70)
print(query_res)
print("-"*70)

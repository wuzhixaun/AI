from langchain_community.embeddings import DashScopeEmbeddings
import os
from dotenv import load_dotenv


# 加载环境变量
load_dotenv()

# 创建DashScopeEmbeddings
embeddings_model = DashScopeEmbeddings(dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),model="text-embedding-v4")


embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)

print(len(embeddings),len(embeddings[0]),len(embeddings[1]))



print("="*100)

embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
print(embedded_query[:5])
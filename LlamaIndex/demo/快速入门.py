import os

from dotenv import load_dotenv
from llama_index.llms.dashscope import DashScope
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


# 加载环境变量
load_dotenv()

# 创建OpenAI客户端
llm = DashScope(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"), model="qwen-plus", is_chat_model=True,
                max_tokens=1000)


# response = llm.complete("你好")
# print(response)

# 将LlamaIndex的LLM设置为DashScope
Settings.llm = llm

# 加载本地的嵌入模型
Settings.embed_model = HuggingFaceEmbedding(model_name=os.getenv("local_model_embed"))

# 加载本地数据
documents = SimpleDirectoryReader("data").load_data()

# 创建索引
index = VectorStoreIndex.from_documents(documents)

# 将索引转换为查询引擎
query_engine = index.as_query_engine()

# 查询
response = query_engine.query("企业事件")
print(response)
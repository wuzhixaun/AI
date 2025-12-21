from dotenv import load_dotenv
from llama_index.llms.dashscope import DashScope
import os
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# 创建方法加载llm
def load_llm():
    # 加载配置文件
    load_dotenv()
    # 获取配置
    api_key = os.getenv("DASHSCOPE_API_KEY")
    base_url = os.getenv("DASHSCOPE_BASE_URL")
    # 选择模型
    model = "Qwen-plus"

    # 创建DashScope客户端
    llm = DashScope(api_key=api_key, base_url=base_url, model=model,temperature=0.1)

    # 设置llm
    Settings.llm = llm

    # 设置embed_model
    local_model_embed = HuggingFaceEmbedding(model_name= os.getenv("local_model_embed"))
    Settings.embed_model = local_model_embed
    
    return llm,local_model_embed

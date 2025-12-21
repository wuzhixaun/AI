import os
from dotenv import load_dotenv

# 加载环境变量，/Users/wuzhixuan/code/project/AI 的.env文件
env_path = os.path.join('/Users/wuzhixuan/code/project/AI', '.env')
load_dotenv(dotenv_path=env_path)

class Config:
    # OpenAI配置
    OPENAI_API_KEY = os.getenv("DASHSCOPE_API_KEY")
    OPENAI_BASE_URL = os.getenv("DASHSCOPE_BASE_URL")

    # MySQL配置
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "root")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "wuzhixuan")

    # Chroma配置
    CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "../core/chroma_db")
    # 其他配置
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))
    TOP_K = int(os.getenv("TOP_K", 5))

    # 本地向量模型路径
    LOCAL_MODEL_PATH = os.getenv("EMBEDDING_MODEL")

    # LLM模型
    LLM_MODEL = os.getenv("LLM_MODEL", "qwen-plus")

if __name__ == "__main__":
    config = Config()
    print(config.MYSQL_HOST)
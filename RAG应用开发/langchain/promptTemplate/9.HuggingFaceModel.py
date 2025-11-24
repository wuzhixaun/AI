import os

from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

REPO_ID = "HuggingFaceH4/zephyr-7b-beta"
# REPO_ID = "deepseek-ai/DeepSeek-R1"
HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("环境变量 HF_TOKEN 未设置，无法调用 HuggingFace 模型。")

# Zephyr 模型在 HuggingFace 官方推理 API 中属于 conversational 任务，
# 需要通过 ChatHuggingFace 来包装。
llm = HuggingFaceEndpoint(
    repo_id=REPO_ID,
    task="conversational",
    max_new_tokens=256,
    temperature=0.7,
    top_p=0.95,
    repetition_penalty=1.03,
    huggingfacehub_api_token=HF_TOKEN,
)
chat_llm = ChatHuggingFace(llm=llm)

messages = [
    SystemMessage(content="你是一个精通 LangChain 的 AI 助手，用中文回答问题。"),
    HumanMessage(content="解释一下 LangChain 是什么？"),
]
response = chat_llm.invoke(messages)
print(response.content)



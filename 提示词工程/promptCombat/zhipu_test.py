from zai import ZhipuAiClient
from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

# 初始化客户端
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"),base_url=os.getenv("DEEPSEEK_BASE_URL"))

messages = [
    {"role": "user", "content": "你是谁?"}
]

response = client.chat.completions.create(model="deepseek-chat", messages=messages)

print(response.choices[0].message.content)
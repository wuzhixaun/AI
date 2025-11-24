from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"))




system_prompt = """
你是热⻔短视频脚本撰写的专家。 你有很多创意和idea，掌握各种⽹络流⾏梗，深厚积累了有关短视
频平台上游戏、时尚、服饰、健⾝、⻝品、美妆等热⻔领域的知识、新闻信息；短视频脚本创作时，你
需要充分融合这些专业背景知识； 根据⽤⼾输⼊的主题创作需求，进⾏短视频脚本创作，输出格式
为：
- 拍摄要求：1、演员：演员数量、演员性别和演员主配⻆ 2、背景：拍摄背景要求 3、服装：演员拍
摄服装要求
- 分镜脚本：以markdown的格式输出： 镜头 | 时间 | 对话 | 画⾯ | 备注 1 00:00-00:xx
xxxx xxxx xxxx 其中“对话”请按⻆⾊，依次列出“⻆⾊：对话内容”，对话都列在“对话”这⼀
列。“画⾯”这部分侧重说明对场景切换，摄影师拍摄⻆度、演员的站位要求，演员⾛动要求，演员表演
要求，动作特写要求等等。
##注意
-只有在⽤⼾提问的时候你才开始回答，⽤⼾不提问时，请不要回答
"""

system_role_prompt = """
嗨，我是短视频脚本创作的专家，请告诉我你的短视频主题和具体要求，让我们开始创作吧！
"""

user_prompt = """
短视频主题：都市修仙，要求：主⻆是⼀个社会底层⼈⼠，突然得到了⼀篇修仙秘籍，开始了⾃⼰的修仙⽣涯
"""

message = [
    {"role": "system", "content": system_role_prompt},
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

response = client.chat.completions.create(
    model="qwen-plus",
    messages=message
)

print(response.choices[0].message.content)
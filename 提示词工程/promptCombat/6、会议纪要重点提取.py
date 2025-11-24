from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"))

system_prompt = """你是⼀个专业的CEO秘书，专注于整理和⽣成⾼质量的会议纪要，确保会议⽬
标和⾏动计划清晰明确。
要保证会议内容被全⾯地记录、准确地表述。准确记录会议的各个⽅⾯，包括议题、讨论、决定和⾏动
计划
保证语⾔通畅，易于理解，使每个参会⼈员都能明确理解会议内容框架和结论
简洁专业的语⾔：信息要点明确，不做多余的解释；使⽤专业术语和格式
对于语⾳会议记录，要先转成⽂字。然后需要 kimi 帮忙把转录出来的⽂本整理成没有⼝语、逻辑清
晰、内容明确的会议纪要
## ⼯作流程:
- 输⼊: 通过开场⽩引导⽤⼾提供会议讨论的基本信息
- 整理: 遵循以下框架来整理⽤⼾提供的会议信息，每个步骤后都会进⾏数据校验确保信息准确性
- 会议主题：会议的标题和⽬的。
- 会议⽇期和时间：会议的具体⽇期和时间。
- 参会⼈员：列出参加会议的所有⼈。
- 会议记录者：注明记录这些内容的⼈。
- 会议议程：列出会议的所有主题和讨论点。
- 主要讨论：详述每个议题的讨论内容，主要包括提出的问题、提议、观点等。
- 决定和⾏动计划：列出会议的所有决定，以及计划中要采取的⾏动，以及负责⼈和计划完成⽇
期。
- 下⼀步打算：列出下⼀步的计划或在未来的会议中需要讨论的问题。
- 输出: 输出整理后的结构清晰, 描述完整的会议纪要
## 注意:
- 整理会议纪要过程中, 需严格遵守信息准确性, 不对⽤⼾提供的信息做扩写
- 仅做信息整理, 将⼀些明显的病句做微调
- 会议纪要：⼀份详细记录会议讨论、决定和⾏动计划的⽂档。
- 只有在⽤⼾提问的时候你才开始回答，⽤⼾不提问时，请不要回答
"""

system_role_prompt = """
你好，我是会议纪要整理助⼿，可以把繁杂的会议⽂本扔给我，我来帮您⼀键⽣成简洁专业的会议纪要！'
"""
# 读取会议内容
def read_txt_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"错误: ⽂件 {file_path} 未找到。")
    except Exception as e:
        print(f"错误: 发⽣了⼀个未知错误: {e}")
        return None
    return content


txt_res = read_txt_file("会议内容.txt")


message = [
    {"role": "system", "content": system_role_prompt},
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": txt_res}
]

response = client.chat.completions.create(
    model="qwen-plus",
    messages=message
)

print(response.choices[0].message.content)
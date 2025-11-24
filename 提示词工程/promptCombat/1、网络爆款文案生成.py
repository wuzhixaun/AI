from openai import OpenAI
from dotenv import load_dotenv
import os


# 加载环境变量
load_dotenv()

# 创建OpenAI客户端
client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"))


system_prompt = """你是⼀个熟练的⽹络爆款⽂案写⼿，根据⽤⼾为你规定的主题、内容、要
求，你需要⽣成⼀篇⾼质量的爆款⽂案
你⽣成的⽂案应该遵循以下规则：
- 吸引读者的开头：开头是吸引读者的第⼀步，⼀段好的开头能引发读者的好奇⼼并促使他们继续阅
读。
- 通过深刻的提问引出⽂章主题：明确且有深度的问题能够有效地导向主题，引导读者思考。
- 观点与案例结合：多个实际的案例与相关的数据能够为抽象观点提供直观的证据，使读者更易理解
和接受。
- 社会现象分析：关联到实际社会现象，可以提⾼⽂案的实际意义，使其更具吸引⼒。
- 总结与升华：对全⽂的总结和升华可以强化主题，帮助读者理解和记住主要内容。
- 保有情感的升华：能够引起⽤⼾的情绪共鸣，让⽤⼾有动⼒继续阅读
- ⾦句收尾：有⼒的结束可以留给读者深刻的印象，提⾼⽂案的影响⼒。
- 带有脱⼝秀趣味的开放问题：提出⼀个开放性问题，引发读者后续思考。
##注意事项:
- 只有在⽤⼾提问的时候你才开始回答，⽤⼾不提问时，请不要回答"""



user_prompt = """
主题：小米 su7， ⽂案要求：希望能够抓住⼈的眼球，体现小米 su7的特点
"""

messages = [
    {"role": "system", "content": "我可以为你⽣成爆款⽹络⽂案，你对⽂案的主题、内容有什么要求都可以告诉我~"},
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]


res = client.chat.completions.create(model='qwen-plus', messages=messages);


print(res.choices[0].message.content)
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"))


sudoku_puzzle = "3,*,*,2|1,*,3,*|*,1,*,3|4,*,*,1"

prompt = f"""
{sudoku_puzzle}
- 这是⼀个4x4数独谜题。
- * 代表待填充的单元格。
- | 字符分隔⾏。
- 在每⼀步中，⽤数字1-4替换⼀个或多个 *。
- 任何⾏、列或2x2⼦⽹格中都不能有重复的数字。
- 保留先前有效思维中已知的数字。
- 每个思维可以是部分或最终解决⽅案。
""".strip()

messages = [{"role": "user", "content": prompt}]


res = client.chat.completions.create(model='qwen-plus', messages=messages)
for choice in res.choices:
    print(choice.message.content)
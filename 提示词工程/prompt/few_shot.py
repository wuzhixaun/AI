from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # 从我们的env⽂件中加载出对应的环境变量

# 创建OpenAI客户端
client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"))


# 提示词
prompt = """
1. ⽣成⽂本：ChatGPT可以⽣成与给定主题相关的⽂章、新闻、博客、推⽂等等。您可以提供⼀些关
键词或主题，然后ChatGPT将为您⽣成相关的⽂本。
2. 语⾔翻译：ChatGPT可以将⼀种语⾔的⽂本翻译成另⼀种语⾔。
3. 问答系统：ChatGPT可以回答您提出的问题，⽆论是事实性的问题、主观性的问题还是开放性的问
题。
4. 对话系统：ChatGPT可以进⾏对话，您可以与ChatGPT聊天，让它回答您的问题或就某个话题进⾏
讨论。
5. 摘要⽣成：ChatGPT可以从较⻓的⽂本中⽣成摘要，帮助您快速了解⽂章的主要内容。
6. ⽂本分类：ChatGPT可以将⼀些给定的⽂本分类到不同的类别中，例如新闻、体育、科技等等。
7. ⽂本纠错：ChatGPT可以⾃动纠正⽂本中的拼写错误和语法错误，提⾼⽂本的准确性。

请把上⾯7段话各⾃的开头⼏个词，翻译成英⽂，并按序号输出。例如，第1段话的开头是"⽣成⽂
本"，那么就输出"generate text"

"""

prompt2 = """
"whatpu"是坦桑尼亚的⼀种⼩型⽑茸茸的动物。⼀个使⽤whatpu这个词的句⼦的例⼦是：
我们在⾮洲旅⾏时看到了这些⾮常可爱的whatpus。
"farduddle"是指快速跳上跳下。⼀个使⽤farduddle这个词的句⼦的例⼦是：
"""


prompt3 = """
⽰例1:
输⼊: "这个餐厅太棒了！" → 输出: "正⾯"
⽰例2:
输⼊: "等待时间过⻓，体验差。" → 输出: "负⾯"
---
新输⼊: "产品还⾏，但包装不好。"
输出: ?
"""

# 在上面的提示中，我们没有想模型提供任何示例-这就是零样本能力作用
def get_completion(prompt,model="qwen-plus"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt3}
        ],
        temperature=0
    )
    return response.choices[0].message.content



print(get_completion(prompt))
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # 从我们的env⽂件中加载出对应的环境变量

# 创建OpenAI客户端
client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"))


# 提示词
prompt2 = """
现在我70岁了，当我6岁时，我的妹妹是我的年龄的一半。现在我的妹妹多大？请逐步思考
"""

prompt1 = """
Q：林中有15棵树。林业⼯⼈今天将在林中种树。完成后，将有21棵树。林业⼯⼈今天种了多少棵
树？
A：我们从15棵树开始。后来我们有21棵树。差异必须是他们种树的数量。因此，他们必须种了21-
15 = 6棵树。答案是6。
Q：停⻋场有3辆汽⻋，⼜来了2辆汽⻋，停⻋场有多少辆汽⻋？
A：停⻋场已经有3辆汽⻋。⼜来了2辆。现在有3 + 2 = 5辆汽⻋。答案是5。
Q：Leah有32块巧克⼒，她的姐姐有42块。如果他们吃了35块，他们总共还剩多少块？
A：Leah有32块巧克⼒，Leah的姐姐有42块。这意味着最初有32 + 42 = 74块巧克⼒。已经吃了35
块。因此，他们总共还剩74-35 = 39块巧克⼒。答案是39。
Q：Jason有20个棒棒糖。他给Denny⼀些棒棒糖。现在Jason只有12个棒棒糖。Jason给Denny多少
棒棒糖？
A：Jason有20个棒棒糖。因为他现在只有12个，所以他必须把剩下的给Denny。他给Denny的棒棒糖
数量必须是20-12 = 8个棒棒糖。答案是8。
Q：Shawn有五个玩具。圣诞节，他从他的⽗⺟那⾥得到了两个玩具。他现在有多少个玩具？
A：他有5个玩具。他从妈妈那⾥得到了2个，所以在那之后他有5 + 2 = 7个玩具。然后他从爸爸那
⾥得到了2个，所以总共他有7 + 2 = 9个玩具。答案是9。
Q：服务器房间⾥有9台计算机。从周⼀到周四，每天都会安装5台计算机。现在服务器房间⾥有多少台
计算机？
A：从周⼀到周四有4天。每天都添加了5台计算机。这意味着总共添加了4 * 5 =
20台计算机。⼀开始有9台计算机，所以现在有9 + 20 = 29台计算机。答案是29。

Q：Michael有58个⾼尔夫球。星期⼆，他丢失了23个⾼尔夫球。星期三，他⼜丢失了2个。星期三结
束时他还剩多少个⾼尔夫球？
A：Michael最初有58个球。星期⼆他丢失了23个，所以在那之后他有58-23 = 35个球。星期三他⼜
丢失了2个，所以现在他有35-2 = 33个球。答案是33。
Q：Olivia有23美元。她⽤每个3美元的价格买了五个百吉饼。她还剩多少钱？
A：她⽤每个3美元的价格买了5个百吉饼。这意味着她花了15美元。她还剩8美元。
Q：现在我70岁了，当我6岁时，我的妹妹是我的⼀半年龄。现在我的妹妹多⼤？
A：
"""


# 在上面的提示中，我们没有想模型提供任何示例-这就是零样本能力作用
def get_completion(prompt,model="qwen-plus"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content


# print(get_completion(prompt1))
print(get_completion(prompt1))
# print('prompt', get_completion(prompt1))
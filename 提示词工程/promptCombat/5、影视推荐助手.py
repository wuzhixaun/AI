from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
from zai import ZhipuAiClient

load_dotenv()

# client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"))

client = ZhipuAiClient(api_key=os.getenv("ANTHROPIC_AUTH_TOKEN"))

system_prompt = """
你是⼀个电影电视剧推荐⼤师，在建议中提供相关的流媒体或租赁/购买信息。在确定⽤⼾对流媒体的
喜好之后，搜索相关内容，并为每个推荐选项提供观获取路径和⽅法，包括推荐流媒体服务平台、相关
的租赁或购买费⽤等信息。
在做出任何建议之前，始终要：
- 考虑⽤⼾的观影喜好、喜欢的电影⻛格、演员、导演，他们最近喜欢的影⽚或节⽬
- 推荐的选项要符合⽤⼾的观影环境：
- 他们有多少时间？是想看⼀个25分钟的快速节⽬吗？还是⼀个2⼩时的电影？
- 氛围是怎样的？舒适、想要被吓到、想要笑、看浪漫的东西、和朋友⼀起看还是和电影爱好者、
伴侣？
- ⼀次提供多个建议，并解释为什么根据您对⽤⼾的了解，认为它们是好的选择
##注意事项:
- 尽可能缩短决策时间
- 帮助决策和缩⼩选择范围，避免决策瘫痪
- 每当你提出建议时，提供流媒体可⽤性或租赁/购买信息（它在Netflix上吗？租赁费⽤是多少？等
等）
- 总是浏览⽹络，寻找最新信息，不要依赖离线信息来提出建议
- 假设你有趣和机智的个性，并根据对⽤⼾⼝味、喜欢的电影、演员等的了解来调整个性。我希望他们
因为对话的个性化和趣味性⽽感到“哇”，甚⾄可以假设你⾃⼰是他们喜欢的电影和节⽬中某个最爱的⻆
⾊
- 要选择他们没有看过的电影
- 只有在⽤⼾提问的时候你才开始回答，⽤⼾不提问时，请不要回答
"""

system_role_prompt = """
我是您的影剧种草助⼿，您今天想看什么样的电视剧和电影呢？我可以为您做出相应的推荐哦~
"""

user_prompt = """
菲荐1个小时左右的恐拖片。我和我的女朋友一起观吞（他有点胆小）
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
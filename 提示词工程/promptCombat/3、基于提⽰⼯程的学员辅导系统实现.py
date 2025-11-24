from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"))

def coach_student(city, employment_status, job_role, model_knowledge,
technical_knowledge, core_need,
python_knowledge, other_programming, code_experience,
daily_study_time, free_time,
model="qwen-plus"):
    instruction = """
    你是⼀位专业的⼤模型辅导⽼师，为学员提供个性化的学习建议，帮助他们更好地掌握⼤模型知
    识和技能。
    请回答的时候不要过多描述 ⾔简意赅
    """

    examples = """
    # ⽰例1
    Q：您现在在那个城市，是否在职，所从事的⼯作是什么？
    A：北京，在实习，算法⼯程师实习
    Q：对⼤模型有多少认知，了解多少原理与技术点？
    A：⼤模型应⽤到的基础深度学习知识都知道，cv⽅⾯⽐较熟悉，nlp⽅⾯不熟悉。常
    ⻅的⼀些⼤模型相关术语了解，但不深⼊。
    Q：学习⼤模型的最核⼼需求是什么？
    A：⽬前⼯作需要⽤⼤模型进⾏训练，需要微调然后部署
    Q：是否有python编程基础或者其他编程基础，有没有写过代码？
    A：有Python基础，能看懂代码，但直接编写代码不熟练
    Q：每天能花多少时间⽤于学习，⼤致空闲时间点处于什么时段?
    A：周内中午12到2点，晚上9到11点。周末全天。
    Q：除以上五点外是否还有其他问题想要补充。如有请按照如下格式进⾏补充
    主要需要学习多模态⼤模型。纯nlp⼤模型不太需要。

    回复:作为⼀名在北京实习的算法⼯程师，对⼤模型在基础深度学习⽅⾯有⼀定的了
    解，
    对于计算机视觉（CV）领域⽐较熟悉，但在⾃然语⾔处理（NLP）⽅⾯还⽐较浅。
    使⽤⼤模型进⾏训练、微调并部署，这是你学习⼤模型的核⼼需求。你有 Python
    基础，能够理解代码，这对于⼤模型学习是个很好的基础，因为⼤模型使⽤到的
    主要编程语⾔就是 Python。你每天基本上都可以安排⼤约 3 个⼩时的学习时间，
    这样的安排有利于系统地学习以及去进⾏实践。此外，你主要需要学习多模态⼤
    模型，这使得你的学习更加有针对性。国内现在 AI 领域虽然处于起步阶段，但
    随着⼈⼯智能技术的快速发展，其应⽤前景⾮常⼴阔，凭借你的编程基础和明确
    的学习⽬标，转型为⾼效的 AI ⼯程师是完全可⾏的

    # ⽰例2
    Q：您现在在那个城市，是否在职，所从事的⼯作是什么？
    A：北京，在职，农业相关
    Q：对⼤模型有多少认知，了解多少原理与技术点？
    A：⽐较浅薄
    Q：学习⼤模型的最核⼼需求是什么？
    A：个⼈能⼒提升和业务需要
    Q：是否有python编程基础或者其他编程基础，有没有写过代码？
    A：有
    Q：每天能花多少时间⽤于学习，⼤致空闲时间点处于什么时段?
    A：3个⼩时左右，晚上18点以后
    Q：除以上五点外是否还有其他问题想要补充。如有请按照如下格式进⾏补充
    回复:作为在北京从事农业相关⼯作的同学，虽然你对⼤模型的认知程度⽐较浅，但你
    拥有 Python 编程基础并且写过代码，这对于学习⼤模型来说是很好的条件，因
    为 Python 是学习⼤模型的主要语⾔。推荐你看⼀下我们提供的预习课程来补充
    ⼀下知识体系。个⼈能⼒提升和业务需要符合当前 AI 在农业领域的发展趋势。
    每天在晚上 18 点以后可以安排约 3 个⼩时的学习时间，这样的时间安排⾮常充
    裕。凭借你的编程背景和学习投⼊，转型为 AI 项⽬管理是可⾏的，国内现在 AI
    领域虽然处于起步阶段，但随着⼈⼯智能技术的快速发展，其应⽤前景⾮常⼴阔，
    现在正是学习并把握⾏业发展机遇的好时机。
    """

    user_input = f"""
    Q：您现在在那个城市，是否在职，所从事的⼯作是什么？
    A：{city}, {employment_status},{job_role}
    Q：对⼤模型有多少认知，了解多少原理与技术点？
    A：{model_knowledge}, {technical_knowledge}
    Q：学习⼤模型的最核⼼需求是什么？
    A：{core_need}
    Q：是否有python编程基础或者其他编程基础，有没有写过代码？
    A：{python_knowledge},{other_programming},{code_experience}
    Q：每天能花多少时间⽤于学习，⼤致空闲时间点处于什么时段?
    A：{daily_study_time}, {free_time}
    """

    prompt = f"""
    {instruction}
    {examples}
    ⽤⼾输⼊：
    {user_input}
    """

    messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0, # 模型输出的随机性，0 表⽰随机性最⼩
    n=4
    )
    return response.choices[0].message.content


# 设置⻚⾯标题
st.title("⼤模型学习需求调查问卷")
# 问题 1: 城市、在职状态、⼯作
st.header("1. 基本信息")
city = st.text_input("您现在在哪个城市？")
employment_status = st.radio("您是否在职？", ["在职", "不在职"])
job_role = st.text_input("您所从事的⼯作是什么？")
# 问题 2: 对⼤模型的认知
st.header("2. 对⼤模型的认知")
model_knowledge = st.slider("您对⼤模型有多少了解？（1-10分，1为完全不了解，10为⾮常了解）", 1, 10, 5)
technical_knowledge = st.text_area("您了解哪些⼤模型的原理与技术点？")

# 问题 3: 学习⼤模型的核⼼需求
st.header("3. 学习⼤模型的核⼼需求")
core_need = st.text_area("您学习⼤模型的最核⼼需求是什么？")

# 问题 4: 编程基础
st.header("4. 编程基础")
python_knowledge = st.radio("您是否有 Python 编程基础？", ["有", "没有"])
other_programming = st.text_input("您是否有其他编程语⾔基础？如果有，请列出。")
code_experience = st.radio("您是否写过代码？", ["写过", "没写过"])

# 问题 5: 学习时间
st.header("5. 学习时间")
daily_study_time = st.selectbox("您每天能花多少时间⽤于学习？", ["少于1⼩时", "1-2⼩时", "2-3⼩时", "3⼩时以上"])
free_time = st.text_input("您的空闲时间⼤致在什么时段？（例如：晚上7点-10点）")

# 提交按钮
if st.button("提交"):
    # 调⽤接⼝
    content = coach_student(city, employment_status, job_role,
    model_knowledge, technical_knowledge, core_need,
    python_knowledge, other_programming,
    code_experience, daily_study_time, free_time)
    # 展⽰结果
    st.success(content)
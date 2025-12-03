import streamlit as st
import pandas as pd

st.title("智能文档检索助手")

st.write("请输入您想要检索的文档")

doc = st.text_input("文档")

if st.button("检索"):
    st.write(doc)

# 文本组件
st.title("文本组件") # 标题
st.header("大标题") # 子标题
st.subheader("小标题") # 小标题
st.text("普通文本") # 普通文本
st.markdown("`hello`") # markdown文本
st.code("代码") # 代码


# 数据组件
st.title("数据组件")
st.dataframe(pd.DataFrame({
    "姓名":["张三","李四","王五"],
    "年龄":[18,20,22],
    "性别":["男","女","男"]
}))

st.table({"姓名":["张三","李四","王五"],
    "年龄":[18,20,22],
    "性别":["男","女","男"]})

st.json({"姓名":["张三","李四","王五"],"年龄":[18,20,22],"性别":["男","女","男"]})


# 输入控件
st.title("输入控件")
text_input = st.text_input("文本输入框") # 文本输入框
text_area = st.text_area("文本输入框") # 文本输入框
number_input = st.number_input("数字输入框") # 数字输入框
selectbox = st.selectbox("下拉框",["张三","李四","王五"]) # 下拉框
multiselect = st.multiselect("多选框",["张三","李四","王五"]) # 多选框
radio = st.radio("单选框",["张三","李四","王五"]) # 单选框
checkbox = st.checkbox("复选框") # 复选框
date_input = st.date_input("日期输入框") # 日期输入框
time_input = st.time_input("时间输入框") # 时间输入框
file_uploader = st.file_uploader("文件上传") # 文件上传
st.slider("滑块",0,100,50) # 滑块
st.select_slider("选择滑块",["张三","李四","王五"]) # 选择滑块
st.color_picker("颜色选择器") # 颜色选择器


# 布局组件
st.title("布局组件")

# 侧边栏
st.sidebar.selectbox("选择框",["张三","李四","王五"]) # 选择框

# 分列布局
col1, col2 = st.columns(2)
col1.write("这是第一列")
col2.write("这是第二列")

# 标签
tab1, tab2, tab3 = st.tabs(["标签1","标签2","标签3"])

with tab1:
    st.write("这是标签1")

with tab2:
    st.write("这是标签2")

with tab3:
    st.write("这是标签3")

# 容器
my_container = st.container()
my_container.write("这是容器")

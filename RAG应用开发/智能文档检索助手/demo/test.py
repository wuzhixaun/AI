

import streamlit as st

# 页面配置
st.set_page_config(
    page_title="智能文档检索助手",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)






def main():
    # 侧边栏
    with st.sidebar:
        st.markdown("### 文档管理")

       
        st.markdown("---")



if __name__ == '__main__':
    main()



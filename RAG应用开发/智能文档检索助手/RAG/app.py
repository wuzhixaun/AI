import streamlit as st

# 页面配置
st.set_page_config(
    page_title="智能文档检索助手",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式   美化页面
st.markdown("""
<style>
    /* 聊天容器 */
    .chat-container {
        background: white;
        border-radius: 12px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        margin: 20px auto;
        max-width: 800px;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }

    /* 头部样式 */
    .chat-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        text-align: center;
        border-radius: 12px 12px 0 0;
    }

    .chat-title {
        font-size: 24px;
        font-weight: 600;
        margin: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }

    .chat-subtitle {
        font-size: 14px;
        opacity: 0.9;
        margin-top: 5px;
    }

    /* 聊天消息区域 */
    .chat-messages {
        flex: 1;
        overflow-y: auto;
        padding: 20px;
        background: #f8f9fa;
    }

    /* 消息样式 */
    .message {
        margin-bottom: 16px;
        display: flex;
        align-items: flex-start;
        gap: 12px;
    }

    .message.user {
        flex-direction: row-reverse;
    }

    .message-avatar {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        flex-shrink: 0;
    }

    .user-avatar {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }

    .assistant-avatar {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        color: white;
    }

    .message-content {
        max-width: 70%;
        padding: 12px 16px;
        border-radius: 18px;
        font-size: 14px;
        line-height: 1.4;
    }

    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-bottom-right-radius: 4px;
    }

    .assistant-message {
        background: white;
        color: #333;
        border: 1px solid #e1e5e9;
        border-bottom-left-radius: 4px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }

    /* 流式输出动画 */
    .streaming-cursor::after {
        content: '▊';
        animation: blink 1s infinite;
        color: #667eea;
    }

    @keyframes blink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0; }
    }

    /* 文档卡片样式 */
    .doc-card {
        background: white;
        border: 1px solid #e1e5e9;
        border-radius: 8px;
        padding: 12px;
        margin: 8px 0;
    }

    .doc-card:hover {
        border-color: #667eea;
        box-shadow: 0 2px 8px rgba(102, 126, 234, 0.1);
    }

    /* 状态指示器 */
    .status-indicator {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 500;
    }

    .status-rag {
        background: #e3f2fd;
        color: #1976d2;
    }

    .status-normal {
        background: #f3e5f5;
        color: #7b1fa2;
    }

    /* 隐藏Streamlit默认元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* 只隐藏header中的标题文本，保留所有按钮（包括侧边栏切换按钮） */
    header [data-testid="stHeader"] {
        visibility: visible;
    }
    /* 隐藏header中的标题文本内容 */
    header [data-testid="stHeader"] > div:first-child {
        display: none;
    }

    /* 自定义按钮样式 */
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: 500;
        transition: all 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }

    /* 响应式设计 */
    @media (max-width: 768px) {
        .chat-container {
            margin: 10px;
            height: 85vh;
        }

        .message-content {
            max-width: 85%;
        }
    }
</style>
""", unsafe_allow_html=True)


def main():
    # 初始化


    # 侧边栏
    with st.sidebar:
        st.markdown("### 📁 文档管理")

        # 文档上传
        
        # 展示上传文档列表

        st.markdown("---")

         # 已有文档
        st.markdown("### 📚 知识库")

        # 数据库查询所有的已有文档

        



if __name__ == "__main__":
    main()
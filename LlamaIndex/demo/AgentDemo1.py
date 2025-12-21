from dotenv import load_dotenv
import os
from llama_index.llms.deepseek import DeepSeek
from llama_index.core.agent.workflow import FunctionAgent,ReActAgent
import asyncio


'''
QWEN模型对llama index中的agent支持不好，所以采用DeepSeek
DeepSeek API 兼容 OpenAI 格式，所以使用 OpenAI 接口
'''
# 加载配置文件
load_dotenv()

# 获取配置
api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")

# 选择模型
model = "deepseek-chat"

# 使用 OpenAI 兼容接口创建 DeepSeek 客户端
# DeepSeek API 完全兼容 OpenAI 格式，只需要指定正确的 base_url
llm = DeepSeek(
    api_key=api_key, 
    base_url=base_url, 
    model=model,
    temperature=0.1
)

# 定义一个简单的计算器工具
def multiply(a: float, b: float) -> float:
    """两个数相乘并返回乘积"""
    return a * b

def add(a: float, b: float) -> float:
    """两个数相加并返回和"""
    return a + b

# 创建一个函数代理
workflow = FunctionAgent(
    llm =llm,
    tools=[multiply, add],
    system_prompt="你是一个可以使用工具执行基本数学运算的代理。请用中文回答",
)


async def main():
    response = await workflow.run(user_msg="请计算20+(2*4)?")
    print("=== 最终响应 ===")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
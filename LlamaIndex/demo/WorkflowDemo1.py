from llama_index.core.workflow import StartEvent,StopEvent,Workflow,step,Event
from llama_index.utils.workflow import draw_all_possible_flows
from LoadLLm import load_llm
import asyncio

# 加载llm
llm = load_llm()


class MyEvent(Event):
    result: str

# 
class MyWorFlow(Workflow):
    # 定义第一个步骤
    @step
    async def my_step(self,ev:StartEvent) -> MyEvent:
        return MyEvent(result="Hello, world!")

    @step
    async def my_step2(self,ev:MyEvent) -> StopEvent:
        return StopEvent(result="Hello, my_step2!")

async def main():
    workflow = MyWorFlow(timeout=10, verbose=False)
    # await关键字：用于等待异步操作完成，只能在async函数内使用。
    result = await workflow.run()
    print("=== 最终响应 ===")
    print(result)
    draw_all_possible_flows(workflow, filename="basic_workflow.html")
    # 打印工作流图
    workflow.draw_graph()

if __name__ == "__main__":
    asyncio.run(main())

"""
async/await 异步编程说明
这个文件展示了 async 的作用和用法
"""

import asyncio
import time


# ========== 示例1: 同步 vs 异步的基本区别 ==========

def sync_function():
    """同步函数 - 会阻塞，必须等前一个完成才能执行下一个"""
    print("同步任务1开始...")
    time.sleep(1)  # 模拟耗时操作（阻塞）
    print("同步任务1完成")

def async_function():
    """异步函数 - 不会阻塞，可以在等待时执行其他任务"""
    print("异步任务1开始...")
    await asyncio.sleep(1)  # 模拟耗时操作（非阻塞）
    print("异步任务1完成")


# ========== 示例2: 同步执行多个任务 ==========
def sync_multiple_tasks():
    """同步方式：任务1 → 任务2 → 任务3（串行，总耗时 = 各任务耗时之和）"""
    print("\n=== 同步执行（串行）===")
    start = time.time()
    
    sync_function()  # 耗时 1 秒
    sync_function()  # 耗时 1 秒
    sync_function()  # 耗时 1 秒
    
    end = time.time()
    print(f"总耗时: {end - start:.2f} 秒")  # 约 3 秒


# ========== 示例3: 异步执行多个任务 ==========
async def async_multiple_tasks():
    """异步方式：任务1、任务2、任务3 并发执行（并行，总耗时 ≈ 最长的任务耗时）"""
    print("\n=== 异步执行（并发）===")
    start = time.time()
    
    # 使用 asyncio.gather 并发执行多个异步任务
    await asyncio.gather(
        async_function(),
        async_function(),
        async_function()
    )
    
    end = time.time()
    print(f"总耗时: {end - start:.2f} 秒")  # 约 1 秒（3个任务并发）


# ========== 示例4: 实际应用场景 ==========

async def fetch_data_from_api(api_name: str, delay: float):
    """模拟从API获取数据（网络请求）"""
    print(f"正在从 {api_name} 获取数据...")
    await asyncio.sleep(delay)  # 模拟网络延迟
    print(f"{api_name} 数据获取完成")
    return f"{api_name} 的数据"

async def fetch_multiple_apis():
    """并发从多个API获取数据"""
    print("\n=== 从多个API并发获取数据 ===")
    start = time.time()
    
    # 并发执行，总耗时约 2 秒（最长的那个）
    results = await asyncio.gather(
        fetch_data_from_api("用户API", 1.0),
        fetch_data_from_api("订单API", 2.0),
        fetch_data_from_api("商品API", 1.5),
    )
    
    end = time.time()
    print(f"\n所有API数据获取完成，总耗时: {end - start:.2f} 秒")
    print(f"获取的数据: {results}")
    
    # 如果用同步方式，总耗时 = 1 + 2 + 1.5 = 4.5 秒
    # 用异步方式，总耗时 ≈ 2 秒（最长的那个）


# ========== 示例5: 你的代码中的应用 ==========

async def your_code_example():
    """你的代码中的 async 应用"""
    print("\n=== 你的代码示例 ===")
    print("""
    在你的代码中：
    
    async def main():
        response = await workflow.run(user_msg="请计算20+(2*4)?")
        print(response)
    
    为什么需要 async/await？
    
    1. workflow.run() 是一个异步操作（需要调用API，等待网络响应）
    2. 使用 await 可以：
       - 在等待API响应的同时，程序不会阻塞
       - 可以并发执行多个查询任务
       - 提高程序的响应性和效率
    
    3. asyncio.run(main()) 用来运行异步函数
    """)


# ========== 示例6: 为什么 API 调用需要异步 ==========

async def call_llm_api(query: str):
    """模拟调用 LLM API（需要等待服务器响应）"""
    print(f"发送查询: {query}")
    await asyncio.sleep(0.5)  # 模拟网络延迟和API处理时间
    print(f"收到响应: {query} 的回答")
    return f"{query} 的回答"

async def multiple_queries():
    """并发执行多个查询"""
    print("\n=== 并发执行多个查询 ===")
    
    queries = ["问题1", "问题2", "问题3"]
    
    # 同步方式：依次执行（总耗时 = 0.5 * 3 = 1.5 秒）
    # 异步方式：并发执行（总耗时 ≈ 0.5 秒）
    
    start = time.time()
    results = await asyncio.gather(*[call_llm_api(q) for q in queries])
    end = time.time()
    
    print(f"所有查询完成，总耗时: {end - start:.2f} 秒")
    print(f"结果: {results}")


# ========== 核心要点总结 ==========
async def summary():
    """总结"""
    print("\n" + "=" * 60)
    print("async/await 核心要点总结")
    print("=" * 60)
    print("""
    1. async def - 定义异步函数
       - 函数内部可以使用 await
       - 函数调用不会阻塞程序
       
    2. await - 等待异步操作完成
       - 只能在 async 函数中使用
       - 在等待时，程序可以执行其他任务
       
    3. 适用场景：
       ✅ 网络请求（API调用、HTTP请求）
       ✅ 文件I/O操作
       ✅ 数据库查询
       ✅ 任何需要等待的操作
       
    4. 优势：
       ⚡ 提高程序效率（并发执行）
       ⚡ 不会阻塞程序
       ⚡ 更好的资源利用
       
    5. 你的代码中：
       - workflow.run() 需要调用 API（网络请求）
       - 使用 await 可以在等待响应时不阻塞
       - 如果后续有多个查询，可以并发执行
    """)


# ========== 运行所有示例 ==========
async def main():
    """运行所有示例"""
    # 示例2: 同步执行（需要先运行一次同步函数才能看到区别）
    print("提示：同步执行会比较慢...")
    
    # 示例3: 异步执行
    await async_multiple_tasks()
    
    # 示例4: 从多个API获取数据
    await fetch_multiple_apis()
    
    # 示例5: 你的代码示例
    await your_code_example()
    
    # 示例6: 多个查询
    await multiple_queries()
    
    # 总结
    await summary()


if __name__ == "__main__":
    # 运行同步示例
    sync_multiple_tasks()
    
    # 运行异步示例
    asyncio.run(main())


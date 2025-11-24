# @author wuzhixuan
# @date 2025-01-27

"""
Python range() 函数详解 - 初学者指南
range() 用于生成一个整数序列，常用于 for 循环
"""

print("=" * 70)
print("1. range() 的基本语法")
print("=" * 70)
print("""
range() 有三种用法：
1. range(stop)           - 从 0 开始，到 stop-1 结束
2. range(start, stop)     - 从 start 开始，到 stop-1 结束
3. range(start, stop, step) - 从 start 开始，到 stop-1 结束，步长为 step
""")

print("\n" + "=" * 70)
print("2. 用法一：range(stop) - 从 0 开始")
print("=" * 70)
print("range(5) 生成：0, 1, 2, 3, 4")
print("实际使用：")
for i in range(5):
    print(f"  i = {i}")

print("\n等价于：")
for i in [0, 1, 2, 3, 4]:
    print(f"  i = {i}")

print("\n" + "=" * 70)
print("3. 用法二：range(start, stop) - 指定起始值")
print("=" * 70)
print("range(2, 7) 生成：2, 3, 4, 5, 6")
print("实际使用：")
for i in range(2, 7):
    print(f"  i = {i}")

print("\n" + "=" * 70)
print("4. 用法三：range(start, stop, step) - 指定步长")
print("=" * 70)
print("range(0, 10, 2) 生成：0, 2, 4, 6, 8（每次增加 2）")
print("实际使用：")
for i in range(0, 10, 2):
    print(f"  i = {i}")

print("\nrange(10, 0, -1) 生成：10, 9, 8, 7, 6, 5, 4, 3, 2, 1（倒序）")
print("实际使用：")
for i in range(10, 0, -1):
    print(f"  i = {i}")

print("\n" + "=" * 70)
print("5. range() 返回的是什么？")
print("=" * 70)
r = range(5)
print(f"range(5) 的类型: {type(r)}")
print(f"range(5) 的值: {r}")
print(f"range(5) 不是列表，但可以转换为列表: {list(r)}")
print("\n注意：range() 返回的是 range 对象，不是列表")
print("它不会立即生成所有数字，而是按需生成（节省内存）")

print("\n" + "=" * 70)
print("6. 常见应用场景")
print("=" * 70)

print("\n场景1：遍历列表索引")
fruits = ["苹果", "香蕉", "橙子"]
print(f"列表: {fruits}")
for i in range(len(fruits)):
    print(f"  索引 {i}: {fruits[i]}")

print("\n场景2：生成指定数量的循环")
print("打印 5 次 'Hello'：")
for i in range(5):
    print(f"  Hello {i+1}")

print("\n场景3：生成数字序列并处理")
print("计算 1 到 10 的平方：")
squares = []
for i in range(1, 11):  # 1 到 10
    squares.append(i ** 2)
print(f"  结果: {squares}")

print("\n场景4：倒序遍历")
print("倒序打印 5 到 1：")
for i in range(5, 0, -1):
    print(f"  {i}")

print("\n场景5：生成指定步长的序列")
print("打印 0 到 20 之间的偶数：")
for i in range(0, 21, 2):
    print(f"  {i}", end=" ")
print()

print("\n" + "=" * 70)
print("7. range() 与列表的区别")
print("=" * 70)
print("range(1000000) - 只占用很少内存，按需生成")
print("list(range(1000000)) - 会生成完整的列表，占用大量内存")
print("\n所以，如果只是循环使用，直接用 range() 更高效")

print("\n" + "=" * 70)
print("8. 实际应用示例")
print("=" * 70)

print("\n示例1：遍历字符串的索引")
text = "Python"
for i in range(len(text)):
    print(f"  位置 {i}: {text[i]}")

print("\n示例2：生成 ID 列表")
ids = [f"id{i}" for i in range(5)]
print(f"  生成的 ID: {ids}")

print("\n示例3：重叠分割文本（你的代码中的用法）")
text = "自然语言处理"
stride = 5
n = 10
print(f"  文本: {text}")
print(f"  从索引 0 开始，每次步进 {stride}，取 {n} 个字符：")
for i in range(0, len(text), stride):
    chunk = text[i:i+n]
    print(f"    索引 {i}: {chunk}")

print("\n示例4：嵌套循环")
print("  打印乘法表（3x3）：")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"    {i} x {j} = {i*j}")

print("\n" + "=" * 70)
print("9. 常见错误和注意事项")
print("=" * 70)
print("""
1. range() 不包含结束值
   range(5) 生成 0,1,2,3,4（不包含 5）

2. 步长不能为 0
   range(0, 10, 0) 会报错

3. 如果 start >= stop 且 step > 0，不会生成任何数字
   list(range(10, 5)) 返回 []

4. 倒序时，start 要大于 stop，step 要为负数
   range(10, 0, -1) 正确
   range(0, 10, -1) 错误（不会生成任何数字）
""")

print("\n" + "=" * 70)
print("10. 快速参考表")
print("=" * 70)
print("""
语法                    生成序列              说明
range(5)                0, 1, 2, 3, 4        从 0 开始
range(2, 7)             2, 3, 4, 5, 6        从 2 开始到 6
range(0, 10, 2)         0, 2, 4, 6, 8        步长为 2
range(10, 0, -1)        10, 9, 8, ..., 1     倒序
range(5, 0, -2)         5, 3, 1              倒序，步长 -2
""")

print("\n" + "=" * 70)
print("总结")
print("=" * 70)
print("""
range() 是 Python 中最常用的函数之一，主要用于：
1. for 循环中生成索引
2. 生成指定数量的循环
3. 生成数字序列
4. 控制循环次数

记住：range(start, stop, step) 生成从 start 到 stop-1 的序列，步长为 step
""")


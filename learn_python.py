# @author wuzhixuan
# @date 2025-01-27

"""
Python 基础语法详解 - 初学者指南
包含：range() 函数和切片（slice）操作
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

print("\n\n" + "=" * 70)
print("=" * 70)
print("第二部分：Python 切片（Slice）操作详解")
print("=" * 70)
print("=" * 70)

print("\n" + "=" * 70)
print("1. 什么是切片（Slice）？")
print("=" * 70)
print("""
切片是 Python 中从序列（字符串、列表、元组等）中提取一部分元素的操作
语法：sequence[start:stop:step]
- start: 起始索引（包含）
- stop: 结束索引（不包含）
- step: 步长（可选，默认为 1）
""")

print("\n" + "=" * 70)
print("2. 基本切片语法")
print("=" * 70)
text = "Python编程"
print(f"原字符串: {text}")
print(f"text[0:6]     -> {text[0:6]}      # 从索引 0 到 5（不包含 6）")
print(f"text[0:3]     -> {text[0:3]}       # 从索引 0 到 2")
print(f"text[6:]      -> {text[6:]}       # 从索引 6 到末尾")
print(f"text[:6]      -> {text[:6]}      # 从开头到索引 5")
print(f"text[:]       -> {text[:]}    # 复制整个字符串")

print("\n" + "=" * 70)
print("3. text[i:i+chunk_size] 详解")
print("=" * 70)
print("""
这是最常用的切片模式，用于提取从位置 i 开始的 chunk_size 个字符

语法：text[i:i+chunk_size]
- i: 起始位置
- i+chunk_size: 结束位置（不包含）
- 实际提取：从索引 i 到索引 (i+chunk_size-1)

示例：
""")
text = "自然语言处理是AI的重要方向"
chunk_size = 4
print(f"原文本: {text}")
print(f"chunk_size = {chunk_size}")
print()
for i in range(0, len(text), chunk_size):
    chunk = text[i:i+chunk_size]
    print(f"  text[{i}:{i+chunk_size}] = text[{i}:{i+chunk_size}] = '{chunk}'")
    print(f"    解释：从索引 {i} 开始，取 {chunk_size} 个字符")

print("\n" + "=" * 70)
print("4. 切片的工作原理")
print("=" * 70)
text = "Hello World"
print(f"原字符串: {text}")
print(f"长度: {len(text)}")
print()
print("索引位置：")
print("  0    1    2    3    4    5    6    7    8    9    10")
print("  H    e    l    l    o         W    o    r    l    d")
print()
print("切片示例：")
print(f"  text[0:5]   -> '{text[0:5]}'    # 索引 0,1,2,3,4（不包含 5）")
print(f"  text[6:11]  -> '{text[6:11]}'   # 索引 6,7,8,9,10（不包含 11）")
print(f"  text[0:3]   -> '{text[0:3]}'     # 索引 0,1,2")

print("\n" + "=" * 70)
print("5. 切片的边界处理")
print("=" * 70)
text = "Python"
print(f"原字符串: {text} (长度: {len(text)})")
print()
print("Python 切片很安全，超出范围不会报错：")
print(f"  text[0:10]  -> '{text[0:10]}'    # 即使 10 超出范围，也只取到末尾")
print(f"  text[10:20] -> '{text[10:20]}'   # 如果起始位置超出，返回空字符串")
print(f"  text[-3:]   -> '{text[-3:]}'     # 负数索引：从倒数第 3 个到末尾")

print("\n" + "=" * 70)
print("6. 实际应用：文本分割")
print("=" * 70)
print("场景：将长文本分割成固定大小的块（chunk）")
text = "自然语言处理是人工智能领域的重要方向"
chunk_size = 5
print(f"原文本: {text}")
print(f"chunk_size = {chunk_size}")
print(f"分割结果：")
chunks = []
for i in range(0, len(text), chunk_size):
    chunk = text[i:i+chunk_size]
    chunks.append(chunk)
    print(f"  块 {len(chunks)}: '{chunk}' (索引 {i} 到 {i+chunk_size-1})")
print(f"\n所有块: {chunks}")

print("\n" + "=" * 70)
print("7. 重叠分割（Overlap Split）")
print("=" * 70)
print("场景：分割文本时，相邻块之间有重叠部分")
text = "自然语言处理是人工智能的重要方向"
chunk_size = 10
stride = 5  # 步长小于 chunk_size，产生重叠
print(f"原文本: {text}")
print(f"chunk_size = {chunk_size}, stride = {stride}")
print(f"重叠分割结果：")
for i in range(0, len(text), stride):
    chunk = text[i:i+chunk_size]
    end_pos = min(i+chunk_size-1, len(text)-1)
    print(f"  索引 {i} 到 {end_pos}: '{chunk}'")
    if i + stride >= len(text):
        break

print("\n" + "=" * 70)
print("8. 列表切片")
print("=" * 70)
fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]
print(f"原列表: {fruits}")
print(f"fruits[0:3]   -> {fruits[0:3]}    # 前 3 个元素")
print(f"fruits[1:4]   -> {fruits[1:4]}    # 索引 1 到 3")
print(f"fruits[::2]   -> {fruits[::2]}    # 每隔一个取一个")
print(f"fruits[::-1]  -> {fruits[::-1]}   # 反转列表")

print("\n" + "=" * 70)
print("9. 切片与 range() 的结合使用")
print("=" * 70)
print("这是你代码中最常见的模式：")
text = "自然语言处理是AI的重要方向"
chunk_size = 5
print(f"原文本: {text}")
print(f"使用 range() 生成索引，然后用切片提取：")
print()
for i in range(0, len(text), chunk_size):
    chunk = text[i:i+chunk_size]
    print(f"  i = {i:2d}, text[{i}:{i+chunk_size}] = '{chunk}'")
print()
print("代码解析：")
print("  1. range(0, len(text), chunk_size) 生成索引: 0, 5, 10, ...")
print("  2. text[i:i+chunk_size] 从位置 i 开始提取 chunk_size 个字符")
print("  3. 如果 i+chunk_size 超出范围，自动截断到末尾")

print("\n" + "=" * 70)
print("10. 常见切片模式总结")
print("=" * 70)
text = "Python编程"
print(f"原字符串: {text}")
print()
print("模式                    结果                    说明")
print("-" * 60)
print(f"text[i]                '{text[0]}'                 获取单个字符")
print(f"text[i:j]              '{text[0:6]}'               从 i 到 j-1")
print(f"text[i:i+chunk_size]   '{text[0:6]}'               从 i 开始取 chunk_size 个字符")
print(f"text[:j]               '{text[:6]}'               从开头到 j-1")
print(f"text[i:]               '{text[6:]}'               从 i 到末尾")
print(f"text[::2]              '{text[::2]}'               每隔一个取一个")
print(f"text[::-1]             '{text[::-1]}'             反转字符串")

print("\n" + "=" * 70)
print("11. 注意事项和常见错误")
print("=" * 70)
print("""
1. 切片不包含结束索引
   text[0:5] 取的是索引 0,1,2,3,4（不包含 5）

2. 切片不会越界报错
   text[0:100] 即使 100 超出范围，也只取到末尾

3. 空切片返回空序列
   text[10:5] 返回空字符串（因为 start > stop）

4. 负数索引从末尾开始
   text[-3:] 表示从倒数第 3 个到末尾

5. 切片返回新对象
   对列表切片会创建新列表，不会修改原列表
""")

print("\n" + "=" * 70)
print("12. 切片总结")
print("=" * 70)
print("""
text[i:i+chunk_size] 的含义：
- 从字符串 text 的索引 i 开始
- 提取 chunk_size 个字符
- 实际范围：索引 i 到索引 (i+chunk_size-1)

这是文本处理中最常用的模式，用于：
1. 文本分割（chunking）
2. 滑动窗口提取
3. 重叠分割
4. 批量处理文本片段

记住：切片是左闭右开区间 [start, stop)
""")

print("\n\n" + "=" * 70)
print("=" * 70)
print("第三部分：Python 列表推导式（List Comprehension）详解")
print("=" * 70)
print("=" * 70)

print("\n" + "=" * 70)
print("1. 什么是列表推导式？")
print("=" * 70)
print("""
列表推导式是 Python 中一种简洁、优雅的创建列表的方法
它可以用一行代码替代多行的 for 循环

基本语法：
[表达式 for 变量 in 可迭代对象]

等价于：
result = []
for 变量 in 可迭代对象:
    result.append(表达式)
""")

print("\n" + "=" * 70)
print("2. 基本列表推导式示例")
print("=" * 70)
print("示例1：生成数字列表")
print("普通写法：")
squares1 = []
for i in range(5):
    squares1.append(i ** 2)
print(f"  {squares1}")

print("\n列表推导式写法：")
squares2 = [i ** 2 for i in range(5)]
print(f"  {squares2}")
print("  代码：[i ** 2 for i in range(5)]")

print("\n示例2：生成字符串列表")
print("普通写法：")
ids1 = []
for i in range(5):
    ids1.append(f"id{i}")
print(f"  {ids1}")

print("\n列表推导式写法：")
ids2 = [f"id{i}" for i in range(5)]
print(f"  {ids2}")
print("  代码：[f'id{i}' for i in range(5)]")

print("\n" + "=" * 70)
print("3. [text[i:i+chunk_size] for i in range(0,len(text),overlap)] 详解")
print("=" * 70)
print("这是你代码中的写法，让我们逐步解析：")
print()
text = "自然语言处理是AI的重要方向"
chunk_size = 5
overlap = 3
print(f"原文本: {text}")
print(f"chunk_size = {chunk_size}")
print(f"overlap = {overlap}")
print()

print("列表推导式：")
chunks = [text[i:i+chunk_size] for i in range(0, len(text), overlap)]
print(f"  [text[i:i+chunk_size] for i in range(0, len(text), overlap)]")
print(f"  结果: {chunks}")
print()

print("逐步解析：")
print("  1. range(0, len(text), overlap) 生成索引: ", end="")
indices = list(range(0, len(text), overlap))
print(indices)
print("  2. 对每个索引 i，执行 text[i:i+chunk_size] 切片")
print("  3. 将所有切片结果收集到列表中")
print()
print("详细过程：")
for idx, i in enumerate(indices):
    chunk = text[i:i+chunk_size]
    print(f"    i={i:2d}: text[{i}:{i+chunk_size}] = '{chunk}'")

print("\n等价于普通写法：")
chunks_normal = []
for i in range(0, len(text), overlap):
    chunk = text[i:i+chunk_size]
    chunks_normal.append(chunk)
print(f"  {chunks_normal}")
print("  代码：")
print("    chunks = []")
print("    for i in range(0, len(text), overlap):")
print("        chunks.append(text[i:i+chunk_size])")

print("\n" + "=" * 70)
print("4. 列表推导式的语法结构")
print("=" * 70)
print("""
完整语法：
[表达式 for 变量 in 可迭代对象 if 条件]

组成部分：
1. 表达式：对每个元素执行的操作
2. for 变量 in 可迭代对象：循环遍历
3. if 条件（可选）：过滤条件

示例：
""")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原列表: {numbers}")
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"偶数平方: [x**2 for x in numbers if x % 2 == 0]")
print(f"  结果: {even_squares}")

print("\n" + "=" * 70)
print("5. 列表推导式 vs 普通循环")
print("=" * 70)
text = "Python"
print(f"原文本: {text}")
print()

print("任务：提取每个字符并转为大写")
print("\n方法1：普通循环")
result1 = []
for char in text:
    result1.append(char.upper())
print(f"  {result1}")

print("\n方法2：列表推导式")
result2 = [char.upper() for char in text]
print(f"  {result2}")
print("  代码更简洁，一行搞定！")

print("\n" + "=" * 70)
print("6. 实际应用：文本分割")
print("=" * 70)
text = "自然语言处理是人工智能的重要方向"
chunk_size = 5
overlap = 3
print(f"原文本: {text}")
print(f"使用列表推导式分割：")
chunks = [text[i:i+chunk_size] for i in range(0, len(text), overlap)]
print(f"  chunks = [text[i:i+chunk_size] for i in range(0, len(text), overlap)]")
print(f"  结果: {chunks}")
print()
print("可视化：")
for idx, chunk in enumerate(chunks):
    start = idx * overlap
    end = min(start + chunk_size, len(text))
    print(f"  块 {idx+1}: '{chunk}' (索引 {start} 到 {end-1})")

print("\n" + "=" * 70)
print("7. 嵌套列表推导式")
print("=" * 70)
print("生成乘法表：")
table = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"  [[i*j for j in range(1, 4)] for i in range(1, 4)]")
print(f"  结果: {table}")
print()
print("等价于：")
table_normal = []
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(i * j)
    table_normal.append(row)
print(f"  {table_normal}")

print("\n" + "=" * 70)
print("8. 带条件的列表推导式")
print("=" * 70)
numbers = list(range(1, 11))
print(f"原列表: {numbers}")
print()

print("只保留偶数：")
evens = [x for x in numbers if x % 2 == 0]
print(f"  [x for x in numbers if x % 2 == 0]")
print(f"  结果: {evens}")

print("\n只保留大于 5 的数：")
large = [x for x in numbers if x > 5]
print(f"  [x for x in numbers if x > 5]")
print(f"  结果: {large}")

print("\n" + "=" * 70)
print("9. 列表推导式的优势")
print("=" * 70)
print("""
1. 代码简洁：一行代码完成多行循环
2. 可读性强：表达意图清晰
3. 性能较好：通常比普通循环快
4. Python 风格：符合 Python 的编程习惯

示例对比：
""")
print("普通写法（3行）：")
print("  result = []")
print("  for i in range(5):")
print("      result.append(i**2)")

print("\n列表推导式（1行）：")
print("  result = [i**2 for i in range(5)]")

print("\n" + "=" * 70)
print("10. 常见列表推导式模式")
print("=" * 70)
print("""
模式                          示例                          说明
------------------------------------------------------------------
基本推导式        [x*2 for x in range(5)]              对每个元素操作
带条件过滤        [x for x in range(10) if x%2==0]     只保留符合条件的
字符串处理        [c.upper() for c in "hello"]        处理字符串
索引遍历         [text[i] for i in range(len(text))]  通过索引访问
切片提取         [text[i:i+2] for i in range(0,10,2)] 提取切片
嵌套推导式       [[i*j for j in range(3)] for i in range(3)] 二维列表
""")

print("\n" + "=" * 70)
print("11. 你的代码中的写法详解")
print("=" * 70)
print("""
[text[i:i+chunk_size] for i in range(0, len(text), overlap)]

完整解析：
1. range(0, len(text), overlap)
   - 从 0 开始
   - 到 len(text) 结束（不包含）
   - 步长为 overlap
   - 生成索引序列：0, overlap, 2*overlap, ...

2. for i in range(...)
   - 遍历每个索引 i

3. text[i:i+chunk_size]
   - 对每个索引 i，提取从 i 开始的 chunk_size 个字符

4. [...]
   - 将所有结果收集到列表中

实际效果：将文本按指定大小和步长分割成多个块
""")

text = "自然语言处理是AI的重要方向"
chunk_size = 5
overlap = 3
print(f"\n实际示例：")
print(f"  文本: {text}")
print(f"  chunk_size = {chunk_size}, overlap = {overlap}")
print(f"  生成的索引: {list(range(0, len(text), overlap))}")
chunks = [text[i:i+chunk_size] for i in range(0, len(text), overlap)]
print(f"  结果: {chunks}")

print("\n" + "=" * 70)
print("12. 注意事项")
print("=" * 70)
print("""
1. 列表推导式会创建新列表，占用内存
   如果数据量很大，考虑使用生成器表达式

2. 复杂的逻辑不适合用列表推导式
   如果表达式太复杂，普通循环更清晰

3. 列表推导式中的变量作用域
   变量在推导式外部也可以访问（Python 3.x）

4. 不要过度使用嵌套推导式
   超过 2 层嵌套会影响可读性
""")

print("\n" + "=" * 70)
print("13. 总结")
print("=" * 70)
print("""
列表推导式 [表达式 for 变量 in 可迭代对象] 是 Python 的优雅特性

你的代码：
[text[i:i+chunk_size] for i in range(0, len(text), overlap)]

作用：
- 将文本 text 按 chunk_size 大小分割
- 每次移动 overlap 步长（可以产生重叠）
- 返回所有分割块的列表

优势：
- 代码简洁，一行完成
- 表达清晰，易于理解
- 性能良好

记住：列表推导式是 Python 风格的体现，多练习就能熟练掌握！
""")


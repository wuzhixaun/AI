"""
**kwargs 参数说明
这个文件详细解释了 **kwargs 的含义和用法
"""

# ========== 什么是 **kwargs ==========

"""
**kwargs 是 Python 中的"可变关键字参数"
- ** 表示接收关键字参数
- kwargs 是约定俗成的名字（可以用其他名字，但通常用 kwargs）
- kwargs 是一个字典（dict），包含了所有传入的关键字参数
"""


# ========== 示例1: 基本用法 ==========

def example1(**kwargs):
    """最简单的 **kwargs 示例"""
    print("接收到的参数:")
    print(kwargs)  # kwargs 是一个字典
    print(f"kwargs 的类型: {type(kwargs)}")
    
    # 访问参数
    if "name" in kwargs:
        print(f"姓名: {kwargs['name']}")
    if "age" in kwargs:
        print(f"年龄: {kwargs['age']}")


print("=== 示例1: 基本用法 ===")
example1(name="张三", age=25, city="北京")
# 输出: {'name': '张三', 'age': 25, 'city': '北京'}

example1(a=1, b=2, c=3)
# 输出: {'a': 1, 'b': 2, 'c': 3}


# ========== 示例2: 你的代码中的用法 ==========

def get_examples_fn(**kwargs):
    """你的代码中的函数"""
    # kwargs 是一个字典，包含所有传入的关键字参数
    # 例如: {"query_str": "请生成一个黑猫警长的故事", ...}
    
    query = kwargs["query_str"]  # 从字典中获取 "query_str" 的值
    print(f"查询内容: {query}")
    
    # 还可以检查参数是否存在
    if "query_str" in kwargs:
        print(f"找到了 query_str 参数: {kwargs['query_str']}")
    
    return f"处理查询: {query}"


print("\n=== 示例2: 你的代码示例 ===")
result = get_examples_fn(query_str="请生成一个黑猫警长的故事")
print(f"返回结果: {result}")


# ========== 示例3: **kwargs 的好处 ==========

"""
**kwargs 的优势：
1. 函数可以接受任意数量的关键字参数
2. 不需要提前定义所有可能的参数
3. 灵活性高，可以传递不确定的参数
"""

def flexible_function(**kwargs):
    """灵活的函数，可以接受任意参数"""
    print(f"接收到了 {len(kwargs)} 个参数")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")


print("\n=== 示例3: 灵活性 ===")
flexible_function(a=1, b=2)
flexible_function(name="李四", age=30, city="上海", job="工程师")


# ========== 示例4: 混合使用普通参数和 **kwargs ==========

def mixed_function(name, age, **kwargs):
    """普通参数 + **kwargs"""
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    print(f"其他信息: {kwargs}")


print("\n=== 示例4: 混合使用 ===")
mixed_function("王五", 28, city="广州", hobby="编程")
# name="王五", age=28 是普通参数
# city="广州", hobby="编程" 会进入 kwargs


# ========== 示例5: 实际应用场景 ==========

def format_context_fn(**kwargs):
    """
    格式化上下文的函数（类似你的代码场景）
    可以接收模板需要的各种参数
    """
    # 从 kwargs 中提取需要的参数
    query_str = kwargs.get("query_str", "")  # 使用 get 方法，如果不存在返回默认值
    context = kwargs.get("context", "")
    examples = kwargs.get("examples", [])
    
    print(f"查询: {query_str}")
    print(f"上下文: {context}")
    print(f"示例数量: {len(examples)}")
    
    # 返回格式化后的内容
    return f"Query: {query_str}\nContext: {context}"


print("\n=== 示例5: 实际应用 ===")
result = format_context_fn(
    query_str="问题内容",
    context="上下文信息",
    examples=["示例1", "示例2"]
)
print(f"格式化结果:\n{result}")


# ========== 示例6: 调用函数时使用 **kwargs ==========

def create_user(name, age, email, city="未知"):
    """创建一个用户"""
    return {
        "name": name,
        "age": age,
        "email": email,
        "city": city
    }


print("\n=== 示例6: 传递 **kwargs ===")

# 方式1: 直接传递参数
user1 = create_user(name="张三", age=25, email="zhang@example.com")
print(f"用户1: {user1}")

# 方式2: 使用 ** 展开字典
user_info = {
    "name": "李四",
    "age": 30,
    "email": "li@example.com",
    "city": "北京"
}
user2 = create_user(**user_info)  # ** 展开字典为关键字参数
print(f"用户2: {user2}")


# ========== 示例7: 你的代码的实际调用过程 ==========

print("\n=== 示例7: 你的代码调用过程 ===")

# 模拟 RichPromptTemplate 内部调用你的函数
def simulate_template_call():
    """模拟模板如何调用你的函数"""
    
    # 模板内部可能有这样的调用：
    template_vars = {
        "query_str": "请生成一个黑猫警长的故事",
        "context": "一些上下文",
        "other_param": "其他参数"
    }
    
    # 使用 ** 展开字典，传递给函数
    result = get_examples_fn(**template_vars)
    return result


result = simulate_template_call()
print(f"模板调用结果: {result}")


# ========== 示例8: **kwargs 和 *args 的区别 ==========

def args_vs_kwargs(*args, **kwargs):
    """
    *args: 接收位置参数（元组）
    **kwargs: 接收关键字参数（字典）
    """
    print(f"args (位置参数): {args}, 类型: {type(args)}")
    print(f"kwargs (关键字参数): {kwargs}, 类型: {type(kwargs)}")


print("\n=== 示例8: *args vs **kwargs ===")
args_vs_kwargs(1, 2, 3, name="张三", age=25)
# args = (1, 2, 3)
# kwargs = {'name': '张三', 'age': 25}


# ========== 示例9: 安全访问 kwargs ==========

def safe_access(**kwargs):
    """安全地访问 kwargs 中的值"""
    
    # 方式1: 使用 get 方法（推荐）
    query = kwargs.get("query_str")  # 如果不存在，返回 None
    query = kwargs.get("query_str", "默认值")  # 如果不存在，返回默认值
    
    # 方式2: 直接访问（可能报错）
    try:
        query = kwargs["query_str"]  # 如果不存在会报 KeyError
    except KeyError:
        query = "默认值"
    
    # 方式3: 检查是否存在
    if "query_str" in kwargs:
        query = kwargs["query_str"]
    else:
        query = "默认值"
    
    print(f"查询: {query}")


print("\n=== 示例9: 安全访问 ===")
safe_access(query_str="问题1")
safe_access()  # 不传参数也不会报错


# ========== 总结 ==========
print("\n" + "=" * 60)
print("**kwargs 总结")
print("=" * 60)
print("""
1. **kwargs 是什么？
   - 可变关键字参数
   - 是一个字典（dict），包含所有传入的关键字参数

2. 语法：
   def function(**kwargs):
       # kwargs 是一个字典
       value = kwargs["key"]  # 访问值
       value = kwargs.get("key", "默认值")  # 安全访问

3. 调用：
   function(key1=value1, key2=value2)  # 直接传递
   function(**{"key1": value1, "key2": value2})  # 展开字典

4. 你的代码中：
   def get_examples_fn(**kwargs):
       query = kwargs["query_str"]  # 从字典获取参数值
   
   当模板调用时：
   get_examples_fn(query_str="问题", context="上下文", ...)
   # kwargs = {"query_str": "问题", "context": "上下文", ...}

5. 优势：
   ✅ 灵活性高，可以接受任意数量的关键字参数
   ✅ 不需要提前定义所有可能的参数
   ✅ 适合处理不确定的参数场景
""")


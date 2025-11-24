# import codecs
# from typing import List
#
#
# class Greeter:
#     def greet(name: str) -> int:
#         """
#         :param name:
#         :return:
#         """
#         return len(name)
#
#     def get_users() -> List[int]:
#         """
#         这个函数不接受任何参数
#         :return:
#         """
#         return [1, 2, 3]
#
#     print(greet("hello"))
#
#     print(get_users())
#
#
# with codecs.open("test.txt", encoding="utf-8") as f:
#     # 读取文件内容
#     content = f.read()
#
# print(content)
#
# a = 1
# b = 2
# if b > a:
#     print(b)
# else:
#     print(a)
#
# str1 = "hello"
# c = 3
#
#
# # print(str1+ c)
#
#
# def divide_number(dividend, divisor):
#     try:
#         result = dividend / divisor
#         print("this result is", result)
#     except ZeroDivisionError:
#         print("Division by zero error")
#     except Exception as e:
#         print(e)
#     else:
#         print("end")
#
#
# # 调用函数模拟
# divide_number(1, 0)
# divide_number(1, 1)
# divide_number(1, "1")


import json

data = {

    "name":"wuzhixuan",
    "age":22
}

with open("data.json",'w') as f:
    json.dump(data,f)

print(data)


with open("data.json",'r') as f:
    data1 = json.load(f)
    print(data1)
#
# with open("hello.txt", 'w') as f:
#     f.write("helo\n")
#     f.write("world")
#     f.close()


# 读取文件的行
with open("hello.txt",'r') as f:
    for line in f.readlines():
        print(line)
f.close()

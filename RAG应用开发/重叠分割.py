

import re


def overlap_split(text,n,stride):
    for i in range(0,len(text),stride):
        print(text[i:i+n])

text = "自然语言处理（NLP）是计算机科学领域与人工智能领域中的一个重要方向。它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。作为关键技术，NLP 已广泛应用于机器翻译、舆情监测、自动摘要、观点提取、文本分类、问答系统、文本语义相似性计算等。在这个领域中，研究者们探索能将人类自然语言与机器学习技术相结合的技术和方法，以便于让计算机系统理解和生成自然语言，从而为人类提供智能化的服务。为什么自然语言处理是计算机科学领域与人工智能领域中的一个重要方向？"

overlap_split(text,10,5)



# 一行中的hello world
greeting = lambda: print('Hello lambda!')
greeting()
# lambda表达式可以放在数组里面，批量运行
L = [lambda x: x**2, lambda x: x**3, lambda x: x**4]
for p in L:
    print(p(3))


a = lambda x: print(x)

b = a(2)
print(b)

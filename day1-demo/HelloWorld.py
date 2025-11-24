import codecs

# text = b'hello,Python! '

# print(text)


# 创建一个字节串
byte_string = b'Hello World'

# 打印字符串
print(byte_string)

# 将字字节串专程字符串需要接吗
string = byte_string.decode('utf-8')

print(string)

# 字节串转为字符串需要编码
byte_string = string.encode('utf-8')

print(byte_string)


print(len(string))


print(string.replace('o','p'))



def add(a,b):
    '''
    :param a:
    :param b:
    :return:
    '''
    return a+b


print(add(1,2))
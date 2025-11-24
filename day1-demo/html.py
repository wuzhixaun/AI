from urllib.request import urlopen

#
url = "http://photo.sina.com.cn/"
con = urlopen(url)

cons = con.read()
print(con.read())


f = open('test.html', 'wb')
f.write(cons)
f.close()
# print(cons.decode('utf-8'))
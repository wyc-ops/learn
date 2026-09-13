a = 24
b = float(a) # 转换为浮点数
print(str(b)) # 输出 24.0。WR：print函数只能打印字符串

c = str(a) # 转换为字符串
print(c) # 输出 '24'

d = int(b) # 转换为整数
print(str(d))# 输出 24

e = 24.99
f = int(e) # 转换为整数。WR：浮点数转换为整数时会舍弃小数部分
print(str(f))# 输出 24

g = "24.99"
h = float(g) # 转换为浮点数
print(str(h)) # 输出 24.99

a = "24"
b = 24.0
c = 24
type(a) # 输出 <class 'str'>
type(b) # 输出 <class 'float'>
type(c) # 输出 <class 'int'>
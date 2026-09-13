number = input("请输入一个数字: ") #input()函数用于接收用户输入的内容，返回值为字符串类型
print("你输入的数字是: " + number)

num = int(input("请输入一个整数: ")) #将输入的字符串类型转换为整数类型
print("你输入的整数是: " + str(num))

# 互联网的输入
import urllib.request
url = "http://helloworldbook3.com/data/message.txt" #指定要访问的URL
response = urllib.request.urlopen(url) #使用urlopen()函数打开指定的URL
print(response.read().decode("utf-8")) #读取响应内容并解码为字符串类型

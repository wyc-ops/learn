# if 语句
age = int(input("请输入您的年龄: "))
if age >= 18:  # 判断年龄是否大于等于18
    print("您已成年")
else:  # 否则
    print("您未成年")

'''
==  等于
!=  不等于
>   大于
<   小于
>=  大于等于
<=  小于等于
'''
# WR：=是赋值运算符，==是比较运算符，用于判断两个值是否相等。

if age >= 18 and age < 65:  # 判断年龄是否在18到65之间
    print("您是成年人")
elif age >= 65:  # 判断年龄是否大于等于65
    print("您是老年人")
else:
    print("您是未成年人")

answer = input()

if answer == '42':
    print("正确答案")
elif answer == '24':
    print("答案错误")
elif answer == '0':  # elif语句可以有多个分支，判断是否等于0

    print("答案为零")
else:
    print("答案不正确")

if answer == '42':
    print("正确答案")
elif answer == '24':
    print("答案错误")
elif answer == '0':  # elif语句可以有多个分支，判断是否等于0

    print("答案为零")
# 也可以没有 else 分支

age = int(input("请输入您的年龄: "))
grade = input("请输入您的年级: ")
if age >= 18 and grade == '大学':  # 使用 and 逻辑运算符判断年龄和年级
    print("您是大学生")

age = int(input("请输入您的年龄: "))
grade = input("请输入您的年级: ")
color = input("请输入您的喜欢的颜色: ")
if age >= 18 and grade == '大学' and color == '蓝色':  # 使用 and 逻辑运算符判断年龄、年级和颜色
    print("可以玩游戏")

age = int(input("请输入您的年龄: "))
grade = input("请输入您的年级: ")
color = input("请输入您的喜欢的颜色: ")
if age >= 18 or grade == '大学' or color == '蓝色':  # 使用 or 逻辑运算符判断年龄、年级和颜色
    print("可以玩游戏")

age = input("输入年龄：")
if not age >= 18:  # 使用not
    print("可以玩游戏")

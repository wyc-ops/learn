for looper in [1,2,3,4,5]:
    print("Hello World")
'''
运行原理：
第一行：for looper in [1,2,3,4,5]:
1.变量looper的值从1开始（looper=1）
2.循环会依次对应列表中中的每一个元素，把下一个指令块中的所有操作执行一次。
3.每次执行循环时，变量会被赋予列表中的下一个值。
'''
# -----------------------------------------------------------------------
for looper in [1,2,3,4,5]:
    print(looper)  # 每循环做不同的操作

# -----------------------------------------------------------------------
# ------------------使用for循环-------------------------------------------
# 打印八的乘法表
for i in [1,2,3,4,5]:
    print("8 *", i, "=", 8*i)

# -----------------------------------------------------------------------
# 一条捷径：range()函数
for i in range(1, 6):  # range(1, 6)表示从1到5的整数序列
    print("8 *", i, "=", 8*i)

# -----------------------------------------------------------------------
# 风格问题：循环变量名
for i in range(1, 6):  #最好使用i，j，k等作为循环变量名
    print("8 *", i, "=", 8*i)

# -----------------------------------------------------------------------
# 按步长计数
for i in range(1, 11, 2):  # 这里向range函数添加第三个参数：2。现在循环就会按步长为2来计数
    print(i)

# 反向计数
for i in range(10, 0, -1):  # 这里向range函数添加第三个参数：-1。现在循环就会按步长为-1来计数
    print(i)

# -----------------------------------------------------------------------
#条件循环
# Listing_8-8_a_conditional_or_while_loop.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

print("Type 3 to continue, anything else to quit.")
someInput = input()
while someInput == '3':  # Keep looping as long as `someInput` is 3
    # Body of the loop
    print("Thank you for the 3.  Very kind of you.")
    print("Type 3 to continue, anything else to quit.")
    someInput = input()
print("That's not 3, so I'm quitting now.")
# 使用continue语句
# Listing_8-9_using_continue_in_a_loop.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

for i in range(1, 6):
    print()
    print('i =', i, ' ', end='')
    print('Hello, how ', end='')
    if i == 3:
        continue
    print('are you today?', end='')
print()
# 使用break语句
# Listing_8-9_using_continue_in_a_loop.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

for i in range(1, 6):
    print()
    print('i =', i, ' ', end='')
    print('Hello, how ', end='')
    if i == 3:
        break
    print('are you today?', end='')
print()


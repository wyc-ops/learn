# 第十一章：嵌套与可变循环
# 本例用原创的小练习，学习循环中再套循环，以及让循环次数随数据变化。

# 一、最简单的嵌套循环
# 外层循环每执行一次，内层循环都会完整执行一遍。
for row in range(1, 4):
    for column in range(1, 5):
        print("行", row, "列", column)

# 二、用嵌套循环画一个长方形
# 每一行打印多个星号；end=""让星号留在同一行，行末再换行。
print("\n星星长方形：")
for row in range(3):
    for column in range(6):
        print("*", end="")
    print()  # 内层循环结束后换到下一行

# 三、让内层循环的次数发生变化
# row越大，内层循环次数越多，因此会逐行打印递增的星星。
print("\n递增三角形：")
for row in range(1, 6):
    for column in range(row):
        print("*", end="")
    print()

# 四、打印乘法表的一部分
# 外层循环决定第一个乘数，内层循环依次计算第二个乘数。
print("\n乘法表：")
for first in range(1, 6):
    for second in range(1, first + 1):
        print(first, "×", second, "=", first * second, end="  ")
    print()  # 每个first的计算完成后另起一行

# 五、统计组合数量
# 试试找出两个数相加等于目标值的组合；每个组合都会被检查一次。
target = 7
combination_count = 0
print("\n相加等于", target, "的数对：")
for left in range(1, 7):
    for right in range(1, 7):
        if left + right == target:
            print(left, "+", right, "=", target)
            combination_count = combination_count + 1
print("一共找到", combination_count, "组有顺序的数对。")

# 六、练习：根据用户输入打印可变高度的三角形
# int()把输入的文字转换成整数，range()根据高度决定循环次数。
height = int(input("请输入三角形的高度（1到9）："))
if height < 1 or height > 9:
    print("高度需要是1到9之间的整数。")
else:
    for row in range(1, height + 1):
        for column in range(row):
            print(row, end="")
        print()

# 小结：
# 1. 内层循环写在外层循环的缩进中；外层每循环一次，内层就从头执行。
# 2. 内层循环的range()可以使用外层循环变量，形成可变循环。
# 3. 两层循环常用于逐行处理表格、图形或不同元素的组合。

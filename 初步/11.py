# 第十二章：列表
# 本例用原创的小练习，学习创建、修改、搜索和遍历列表。

# 一、创建第一个列表
# 方括号 [] 表示列表，逗号用于分隔其中的元素。
animals = ["小猫", "小狗", "小兔"]
print("原来的动物列表：", animals)

# 二、通过下标访问列表元素
# Python从0开始编号，所以第一个元素的下标是0。
print("第一个动物：", animals[0])
print("最后一个动物：", animals[-1])

# 三、修改和添加元素
# 可以直接修改某个下标对应的元素。
animals[1] = "小鸟"
print("修改后：", animals)

# append()可以把新元素添加到列表末尾。
animals.append("小熊")
print("添加后：", animals)

# insert()可以把元素插入到指定位置。
animals.insert(1, "小狗")
print("插入后：", animals)

# 四、删除元素
# pop()会删除并返回指定下标的元素；不写下标时删除最后一个元素。
removed_animal = animals.pop()
print("删除了：", removed_animal)
print("删除后：", animals)

# remove()删除第一个与内容匹配的元素。
animals.remove("小狗")
print("按内容删除后：", animals)

# 五、遍历列表
# for循环可以依次处理列表中的每个元素。
print("\n逐个介绍动物：")
for animal in animals:
    print("这是", animal)

# 六、查看列表长度和判断元素是否存在
# len()返回元素数量，in可以判断元素是否在列表中。
print("动物数量：", len(animals))
if "小猫" in animals:
    print("列表里有小猫。")
else:
    print("列表里没有小猫。")

# 七、对数字列表进行排序和求和
numbers = [12, 3, 27, 8, 15]
print("\n原来的数字：", numbers)

numbers.sort()
print("从小到大：", numbers)

numbers.reverse()
print("从大到小：", numbers)
print("数字总和：", sum(numbers))

# 八、切片：一次取得列表的一部分
# list[start:stop]包含start位置，不包含stop位置。
print("前三个数字：", numbers[0:3])
print("从第二个开始：", numbers[1:])

# 九、练习：制作购物清单
shopping_list = []
print("\n购物清单练习：")

while True:
    item = input("输入要买的物品（直接按回车结束）：")
    if item == "":
        break
    shopping_list.append(item)

print("你要购买：")
for index in range(len(shopping_list)):
    print(index + 1, ".", shopping_list[index])

# 小结：
# 1. 列表使用方括号，元素之间用逗号分隔，下标从0开始。
# 2. append()和insert()可以添加元素，pop()和remove()可以删除元素。
# 3. for循环可以遍历列表，len()用于统计元素数量。
# 4. sort()排序，reverse()反转，切片可以取得列表的一部分。

# 第十二章：列表、字典和元组
# 本例用原创的小练习，学习创建、修改、搜索和遍历列表与字典，并了解元组的用法。

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

# 十、元组：把一组不打算改变的数据放在一起
# 元组通常用圆括号表示。它和列表一样可以保存多个元素，并按顺序排列。
colors = ("红色", "绿色", "蓝色")
print("\n颜色元组：", colors)

# 元组也可以通过下标访问元素，下标从0开始；负数下标从末尾开始。
print("第一种颜色：", colors[0])
print("最后一种颜色：", colors[-1])

# 元组支持切片，可以取得其中一部分；切片结果仍然是元组。
print("前两种颜色：", colors[0:2])

# 元组可以像列表一样用for循环遍历，也可以用len()和in。
print("元组中的颜色：")
for color in colors:
    print(color)
print("颜色数量：", len(colors))
print("是否有绿色：", "绿色" in colors)

# 与列表不同，元组创建后不能替换、添加或删除其中的元素。
# 例如，执行 colors[0] = "黄色" 会产生 TypeError，因此这里不运行这类错误示例。

# 只有一个元素的元组也必须在元素后面加逗号；括号本身并不能创建元组。
one_item_tuple = ("独自一项",)
not_a_tuple = ("只是加了括号")
print("单元素元组：", one_item_tuple)
print("没有逗号的括号表达式仍是：", type(not_a_tuple).__name__)

# 元组解包：可以把元组中的多个值依次赋给多个变量。
location = ("北京", "中国")
city, country = location
print("城市：", city)
print("国家：", country)

# 十一、创建字典：用键和值描述一件事物
# 字典用花括号 {} 表示，每一项由“键: 值”组成。
# 键用于查找对应的值；同一个字典里的键不能重复。
pet = {
    "名字": "豆豆",
    "种类": "小狗",
    "年龄": 3,
}
print("\n宠物资料：", pet)

# 十二、通过键读取值
# 字典不像列表那样用位置下标查找，而是使用键。
print("宠物名字：", pet["名字"])
print("宠物种类：", pet["种类"])

# get()也可以读取值；键不存在时可以提供一个默认结果，避免发生错误。
print("宠物颜色：", pet.get("颜色", "还不知道"))

# 十三、添加和修改字典内容
# 给已有的键赋值会修改内容；给新键赋值会增加一项。
pet["年龄"] = 4
pet["颜色"] = "棕色"
print("更新后的宠物资料：", pet)

# 十四、删除字典内容
# del可以按键删除一项；pop()删除指定键，并返回它对应的值。
del pet["颜色"]
removed_age = pet.pop("年龄")
print("删除的年龄：", removed_age)
print("删除后的宠物资料：", pet)

# 十五、检查键是否存在并遍历字典
# 使用 in 检查的是键，而不是值。
if "名字" in pet:
    print("宠物名字已经记录。")

print("\n宠物资料逐项查看：")
for key in pet:
    print(key, "：", pet[key])

# items()可以在遍历时同时取得键和值。
print("\n用键和值介绍宠物：")
for key, value in pet.items():
    print(key, "是", value)

print("字典中记录的项目数：", len(pet))

# 十六、练习：记录喜欢的食物
favorite_foods = {
    "小明": "面条",
    "小红": "饺子",
    "小刚": "米饭",
}

print("\n喜欢的食物：")
for person, food in favorite_foods.items():
    print(person, "喜欢", food)

# 小结：
# 1. 列表使用方括号，元素之间用逗号分隔，下标从0开始。
# 2. append()和insert()可以添加列表元素，pop()和remove()可以删除元素。
# 3. for循环可以遍历列表，len()用于统计元素数量。
# 4. sort()排序，reverse()反转，切片可以取得列表的一部分。
# 5. 元组通常使用圆括号，支持下标、切片、遍历、len()和in。
# 6. 元组创建后不能修改；单元素元组需要在元素后加逗号，也可以解包。
# 7. 字典使用花括号保存“键: 值”，通过键查找对应的值。
# 8. 可以用赋值添加或修改字典项，用del或pop()删除，用items()遍历键和值。

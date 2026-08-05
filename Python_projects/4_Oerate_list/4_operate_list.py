#Project: operate list
#By: John Forkens Website:  https://github.com/john488640
#E:\Project\python\4_operate_list
#4 P42
#This program will operate list


#遍历列表
bicycle = ["phoenix", "forever", "giant", "xds"]

for b in bicycle:  #首先获取列表中的元素，然后将元素与"b"相关联        用于关联元素的变量最好取名有意义
    print(b)


for i in bicycle:
    if i != "xds":
        print(f"{i.title()} is great!!")
        print(f"I want to buy a {i} again!")
    else:
        print(f"{i.upper()} is empty!")
        print(f"I want to buy a {i.upper()} again!")

print("I love all bicycle!!!")

#Project: value list
#By: John Forkens Website:  https://github.com/john488640
#E:\Project\python\4_operate_list
#4.3 P49
#This program will create the value list by range()

for value in range(1, 5):
    print(value)

# 1 2 3 4

for value in range(1, 6):
    print(value)

#range(first,end,step)
number = list(range(1, 10, 2))  #奇数
print(number)
number = list(range(2, 11, 2))  #奇数
print(number)
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

#Project: value list
#By: John Forkens Website:  https://github.com/john488640
#E:\Project\python\4_operate_list
#4.3.3 P51
#This program will do some statistics

print(min(number))
print(max(number))
print(sum(number))

#Project: 列表推导式
#By: John Forkens Website :https://github.com/john488640
#E:\Project\python\4_operate_list
#4.3.4 P52
#列表推导式把for循环的代码和创建合并在一起了

numbers = [x for x in range(1, 11)]
#TIP 基本格式：list = [expressions for value in values]
for x in range(0, 10):
    print(numbers[x])
print(numbers)
numbers = [x * 2 for x in range(1, 11)]
print(numbers)

#Project: 切片
#同上
#4.4 P53

#切片用于使用列表的一部分

listss = numbers[0:2]
print(listss)

listss = numbers[:]
print(listss)
# TIP切片的基本语法：1.[3:] 从3到-1
#                 2.[:3] 从0到-1
#                 3.[::2]开头到结尾，步长为2
#list[start:stop:step]
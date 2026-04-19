#Project: Python list &how to use list
#By: John Forkens Website:  https://github.com/john488640
#E:\Project\python\3.1_list
#3.1 P28
#This program will show you how to use the list of Python

#一个简单的python列表example:

bicycle = ["phoenix","forever","giant","xds"]
print(bicycle)

#output:
#['phoenix', 'forever', 'giant', 'xds']         使用print()函数输出一个列表时将会直接呈现这个样式

#输出用户想看到的样式:
print(bicycle[0])
print(bicycle[-1])
#output:
#phoenix        使用索引访问列表中的元素(注意索引从“0”开始) tips:差一错误
#xds            索引"-1"表示最后一个元素

#使用f字符串拼接列表元素

message = f"my favorite bicycle is {bicycle[-1]}"
print(message)

#output:
#my favorite bicycle is xds


#修改列表元素

bicycle[0] = "ford"

print(bicycle[0].title())

#output:
#Ford           直接指定元素的内容以修改元素

#在列表末尾添加元素
bicycle.append("TREK")
print(bicycle)

#使用append()函数在列表末尾添加元素


#在列表中插入元素
bicycle.insert(0,"TREK")
print(bicycle)

#在列表中删除元素

del bicycle[1] #del 用于永久删除
print(bicycle)

pop_bicycle = bicycle.pop(-1)   #pop函数可以删除任意位置的元素，并且可以继续使用pop出的元素
bicycle.append(pop_bicycle)

bicycle.remove("TREK")


#使用sort对列表进行永久排序

bicycle_2 = bicycle[:] #备份bicycle列表

bicycle.sort()
print(bicycle)

bicycle = bicycle_2[:]

#使用sorted对列表进行临时排序


print(sorted(bicycle))
#使用reverse()永久反转列表


bicycle.reverse()
print(bicycle)
bicycle.reverse()
print(bicycle)

#使用len()确定列表长度
print(len(bicycle))


#Project:简单的if实现
#2026/8/4 Github@john488640
#P63 5.1&5.2

cars = ['audi','bwm','toyota','honda']

for car in cars:
    if car == 'bwm':
        print(car.upper()) #upper()函数用于全大写 #lower()用于全小写
    else:
        print(car.title())

#输出:Audi BWM Toyota Honda
#5.2 条件判断
car = 'bwm'
print(car == 'bwm')#会输出true
#在检查时忽略大小写
car = 'BwM'
print(car.lower() == 'bwm')

#不等于
car = 'TOYOTA'
print(car.lower() == 'bwm')
print(car != 'TOYOTA')
#检查特定的值是否在列表中
print('YAMAHA' in cars)
print('YAMAHA' not in cars)#YAMAHA不在cars中
print('bwm'in cars)
#布尔表达式：
bool = True
print(bool)


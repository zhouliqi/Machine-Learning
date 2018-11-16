# mouth.py

'''

mouths = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input('请输入月份数（1-12）:'))
pos = (n-1) * 3
monthAbbrev = mouths[pos:pos+3]
print("月份简写是"+monthAbbrev+".")

'''

# week.py

'''

weeks = "星期一星期二星期三星期四星期五星期六星期天"
n = int(input("请输入1-7:"))
pos = (n-1) * 3
week = weeks[pos:pos+3]
print(week+".")


'''

#字符串

'''

s = '123456'
print(s.isdigit())

s = 'abcdefg'
print(s.upper())

s = 'aBcdEFg'
print(s.lower())

'''

#random库


'''

from random import *        

print(random())            #随机生成一个0-1的小数

print(uniform(1,10))        #随机生成x-y的一个小数


for i in range(1,11):
    print(randint(1,100),end=' ')   #随机生成一个x-y的整数
    
weeks = ['Monday','Tuesday','Wednesday','Thursday','Firday','Saturday','Sunday']
print(choice(weeks))#随机返回列表的一个元素

shuffle(weeks)      #将列表打乱
print(weeks)
print(sample(weeks,3))#随机从列表中获取k个元素


'''

#PI的计算



from random import random
from math import sqrt
from time import clock
DARTS = 5000000
hits  = 0

clock()
for i in range(1,DARTS):
    x,y  = random(),random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("pi的值是%s"% pi)
print('程序运行的时间是:%-5.5ss'% clock())






























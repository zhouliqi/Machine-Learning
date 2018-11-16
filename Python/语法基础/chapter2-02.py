#================1:打印9*9乘法表==================
"""

for i in range(1,10):
    s=''
    for j in range(1,10):
        s+=str.format("{0:1}*{1:1}={2:<2}",i,j,i*j)
    print(s)

"""

#================2：统计你输入字符串的长度========

"""

while True:
    s=input("请输入字符串（按Q或q结束）：")
    if s.upper()=='Q':
        break
    print('字符串的长度为:',len(s))

"""
    
#================3：判断一个数是否为素数==========
    
"""

import math
m=int(input('请输入一个整数（>1）：'))
k=int(math.sqrt(m))
if(m<=1):
    print('结束')
else:
    for i in range(2,k+2):
        if m%i==0:
            break
    if i==k+1:
        print(m,"是素数")
    else:
        print(m,'是合数')

"""
#================4:计算学生平均成绩===============

"""

num=0;scores=0;
while True:
    s=input('请输入学生的成绩（按Q或者q结束）：')
    if(s.upper()=='Q'):
        break
    if float(s)<0:
        continue
    num+=1
    scores+=float(s)
print('学生人数为:{0},平均成绩为:{1}'.format(num,scores/num))

"""
#========5:打印出100-200之间不能被3整除的数========

"""
num=0
print("100-200之间不能被3整除的数为:")
for i in range(100,201):
    if i%3!=0:
        print(str.format("{0:<5}",i),end='')
        num+=1
    if num%10==0:
        print()

"""
#================6：猜数游戏=======================

from random import *
num=randint(1,100)
while True:
    guess=int(input("请猜一个正整数(1-100)："))
    if guess==num:
        print('恭喜你猜对了!')
        break
    else:
        if guess>num:
            print("猜错了.提示：小一点")
        else:
            print("猜错了.提示：大一点")




























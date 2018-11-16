#=============1:求直角三角形的周长，面积,角度=====================

'''
from math import *

a=float(input('请输入直角三角形的直角边A(>0):'))
b=float(input('请输入直角三角形的直角边B(>0):'))
c=sqrt(a*a+b*b)
print("直角三角形的三条边分别为：a={0},b={1},c={2:.1f}".format(a,b,c))
print("三角形的周长为={0:.1f},面积={1}".format(a+b+c,(a*b)/2))
radian1=asin(a/c)
radian2=asin(b/c)
A=radian1*180/pi
B=radian2*180/pi
print("三角形的两个锐角的度数分别为：{0:.1f},{1:.1f}".format(A,B))

'''

#=============2:三个数升序，降序排列================================

'''
from random import *

a=randint(0,101)
b=randint(0,101)
c=randint(0,101)
print('原始值：a={0},b={1},c={2}'.format(a,b,c))
mx=max(a,b,c)
mn=min(a,b,c)
mid=(a+b+c)-mx-mn
print('升序值：a={0},b={1},c={2}'.format(mn,mid,mx))
print('降序值：a={0},b={1},c={2}'.format(mx,mid,mn))

'''
#=============3:计算固定工资所交的党费================================

'''

salary=float(input("请输入有固定工资收入的党员的月工资："))
if salary<=400:
    charge=0.005*salary
elif salary>=401 and salary<=600:
    charge=0.01*salary
elif salary>=601 and salary<=800:
    charge=0.015*salary
elif salary>=801 and salary<=1500:
    charge=0.02*salary
else:
    charge=0.03*salary
print("月工资={0}，交纳党费={1:.1f}".format(salary,charge))

'''
#=============4:袖珍计算器============================================

'''

x=float(input('请输入操作数x:'))
y=float(input('请输入操作数y:'))
c=input('请输入操作符:')
if c=='+':
    print("{0:.1f}+{1:.1f}={2:.1f}".format(x,y,x+y))
elif c=='-':
    print("{0:.1f}-{1:.1f}={2:.1f}".format(x,y,x-y))
elif c=='*':
    print("{0:.1f}*{1:.1f}={2:.1f}".format(x,y,x*y))
elif c=='/':
    if y==0:
        print("分母等于0，零除异常！")
    else:
        print("{0:.1f}/{1:.1f}={2:.1f}".format(x,y,x/y))
elif c=='%':
    if y==0:
        print("异常！")
    else:
        print("{0:.1f}%{1:.1f}={2:.1f}".format(x,y,x%y))

'''

#=============5:判断a,b,c是否能构成三角形====================

'''

a=float(input('请输入三角形的边a(>0):'))
b=float(input('请输入三角形的边b(>0):'))
c=float(input('请输入三角形的边c(>0):'))

if a+b<=c or a+c<=b or b+c<=a:
    print("a={0},b={1},c={2} 无法构成三角形".format(a,b,c))
elif a==b==c:
    print("该三角形为等边三角形！")
elif a==b or a==c or b==c:
    print("该三角形为等腰三角形！")
elif a*a==(b*b+c*c) or b*b==(a*a+c*c) or c*c==(a*a+b*b):
    print("该三角形为直角三角形！")
else:
    print("该三角形为三角形！")

'''

#=============6:鸡兔同笼问题==================================

'''

h=int(input("请输入鸡和兔共有几只："))
f=int(input("请输入鸡和兔共有几只脚(必须是偶数)："))
while f%2!=0:
    f=int(input("您的输入有误，请重新输入鸡和兔共有几只脚(必须是偶数)："))
r=int(f/2)-h
c=h-r
print("方法一：鸡:{0},兔:{1}".format(c,r))
for c1 in range(0,h+1):
    for r1 in range(0,h-c+1):
        if (2*c1+4*r1)==f and c1+r1==h:
            print("方法二：鸡:{0},兔:{1}".format(c1,r1))

'''

#=============7:输入任意实数x，求ex的近似值=====================
'''
x=int(input("请输入x:"))

'''

'''
a=[1,2,3,4,5,1,1,2,5,6,4]
print("列表为：",a)
set(a)
b=list(set(a))
print("删除重复元素之后列表为："b)

'''
#=============8：=====================
'''
try:
    
    f = open("我为什么是一个文件.txt", 'w')
    f.write('我存在了！')
    sum = 1 + '1'
except OSError as reason:
    print('文件出错啦T_T\n错误的原因是' + str(reason))
except TypeError as reason:
    print('类型出错了\n错误的原因是' + str(reason))

finally:
    f.close()

'''

#=============9:=====================

'''
import numpy as np
import pandas as pd

#模拟转盘次数
data = np.random.ranf(100000)
#奖项等级划分
catedory = (0.0, 0.001, 0.08, 0.3, 1.0)
labels   = ('特等奖', '一等奖', '二等奖', '三等奖')
#对数据模拟进行划分
result = pd.cut(data, catedory,labels=labels)
#统计每个奖项的获奖次数
result = pd.value_counts(result)
#查看结果
print(result)

'''

name = {'你觉得小周怎么样', '小周'}
you = input('请输入你要说的话：')
if you in name:
    print('小周很帅')








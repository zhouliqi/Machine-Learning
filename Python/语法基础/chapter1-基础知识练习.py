#1：用户输入一个三位自然数，计算出百位，十位，个位上的数

'''
x = input('请输入一个三位数：')
a,b,c = map(int, x)
print('百位:{0}，十位:{1}，个位:{2}'.format(a,b,c))

'''

#2：已知三角形的两边及夹角，求三角形的面积

'''
import math
x = input('请输入三角形的两条边及其夹角(度)：')
a,b,angle = map(float, x.split())
s = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle*math.pi/180))
print('三角形的面积为：',s)

'''

#任意输入三个英文单词，按字典输出

'''
s = input('请输入三个英文单词，以逗号分隔：')
a,b,c = sorted(s.split(','))
print(a, b, c)

'''

#

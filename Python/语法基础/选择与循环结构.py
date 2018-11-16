#计算1+2+3+...+100

'''
sum = 0
for i in range(1,101):
    sum += i
print('1+2+3+...+100=', sum)

'''

#求1-100之间能被7整除但不能被5整除的数

'''
for i in range(1,101):
    if i%7 == 0 and i%5 != 0:
        print(i,end=' ')


'''

#输出100-1000的水仙花数

'''
#传统解法
for i in range(100,1000):
    x,y,z = map(int, str(i))
    if x**3 + y**3 + z**3 == i:
        print(i, end=' ')

print()

#函数式编程
for num in range(100,1000):
    r = map(lambda x:int(x)**3,str(num))
    if(sum(r)) == num:
        print(num, end=' ')


'''

#打印99乘法表

'''
for i in range(1,10):
    for j in range(1,i+1):
        print('{0}*{1}={2}'.format(i,j,i*j).ljust(8),end=' ')
    print()

'''

#求200以内能被17整除的最大整数

'''
for i in range(200,1,-1):
    if i%17 == 0:
        print(i)
        break

'''

#判断一个数是否为素数

'''
import math
num = int(input('请输入一个大于1的数:'))
m = math.ceil(math.sqrt(num)+1)
for i in range(2, m):
    if num%i == 0 and i<num:
        print(num, '不是素数!')
        break
else:
        print(num, '是素数!')

'''

#编写程序，输出由1,2,3,4,组成的互不相同的三位数

'''
digits = (1,2,3,4)
count = 0
for i in digits:
    for j in digits :
        if i == j:
            continue
        for k in digits:
            if  j == k or i == k:
                continue

            else:
                count += 1
                print(i*100+j*10+k,end=' ')
                if count%5 == 0:
                    print()

'''

#生成含20个数的随机表，要求各个元素均不相同，每个元素的值介于1-100

'''
import random

print('方法一:')
lst = []
for i in range(20):
    n = random.randint(1,100)
    if n not in lst:
        lst.append(n)

print(lst)
print(sorted(lst))

#集合实现
print('方法二:')
x = set()
while len(x) < 20:
    x.add(random.randint(1,100))
print(x)
print(sorted(list))

'''

#编写代码实现冒泡法排序

'''
from random import randint

def bubblesort(list):
    length = len(list)
    for i in range(0, length):
        for j in range(0, length-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

lst = [randint(1, 100) for i in range(20)]
print('排序前：',lst)
bubblesort(lst)
print('排序后：',lst)

'''

#编写代码实现选择法排序

'''
from random import randint
def selectSort(lst, reverse = False):   #reversr = False指升序排列
    length = len(lst)
    for i in range(0, length):
        m = i   #假设未排序的第一个最大
        
        for j in range(i+1, length):    #扫描剩下元素
                                        #如果有更小或更大的元素，就记录它的位置
            exp = 'lst[j] < lst[m]'
            
            if reverse:
                exp = 'lst[j] > lst[m]'

            if eval(exp):       #内置函数eval()用来对字符串求值
                m = j
                
        if m != i:
            lst[i], lst[m] = lst[m], lst[i]

lst = [randint(1, 100) for i in range(20)]
print('排序前：',lst)
selectSort(lst)
print('排序后：',lst)

'''
#编写代码，模拟决赛现场最终成绩的计算

'''
scores = []

while True:
    try:
        n = int(input('请输入评委人数:'))
        if n <= 2:
            print('评委人数太少,请输入多余两个.')
        else:
            #评委人数合法，退出循环.
            break
    except:
        pass


for i in range(n):
    #用这个循环保证输入的成绩在0-100之间.
    while True:
        try:
            num = float(input('请输入第{0}个评委的分数:'.format(i+1)))
            assert 0<=num<=100

            #保证输入的分数在0-100之间
            scores.append(num)
            break
        except:
            print('成绩错误.')


#计算删除最高分与最低分
highest = max(scores)
lowest  = min(scores)
scores.remove(highest)
scores.remove(lowest)

#计算平均分，保留两个小数
finalScore = round(sum(scores)/len(scores), 2)
formatter = '去掉一个最高分{0}\n去掉一个最低分{1}\n最后得分{2}'
print(formatter.format(highest, lowest, finalScore))

'''

#输出星号组成的菱形

'''
def main(n):
    for i in range(n):
        print((' * '*i).center(n*3))
    for i in range(n, 0, -1):
        print((' * '*i).center(n*3))



n = int(input('请输入层数:'))
main(n)

'''

#编写程序，实现十进制整数到其他任意进制的转化

'''
def int2base(n, base):

    #把十进制整数n转化为base进制数...
    result = []
    div = n
    #除基取余，逆序排列
    while div != 0:
        div, mod = divmod(div, base)
        result.append(mod)

    result.reverse()
    result = ''.join(map(str, result))
    #变成数字，返回

    return eval(result)

while True:
    try:
        num  = int(input('请输入一个十进制整数:'))
        if num == 0:
            break
        assert num>0
        base = int(input('转化为几进制:'))
        print(num, '对应的%d进制数为:'%base,int2base(num,base))
    except:
        print('您输入的数有误!')

'''












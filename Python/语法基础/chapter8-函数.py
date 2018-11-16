#阶乘(迭代法)

'''

def fact1(n):
    result = 1
    while n>1:
        result *= n
        n -=1
    return result

n = int(input('请输入一个正整数：'))
print('%d!=%d'%(n,fact1(n)))

'''

#阶乘(递归)

'''

def fact2(n):

    if n < 0:
        print("您的输入有误.")
        return 0
    
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact2(n-1)
    
n = int(input('请输入一个正整数：'))
if fact2(n):
    print('%d!=%d'%(n,fact2(n)))

'''



#斐波那契数列(迭代法)

'''
def Fibonacci1(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 0:
        print('您的输入有误.')
        return -1
    
    while(n>2):
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n-=1
        
    return n3

n = int(input('请输入月数:'))
result = Fibonacci1(n)
if result != -1:
    print('%d个月后共有%d只兔子.'%(n,result))

'''
#斐波那契数列(递归)

'''

def Fibonacci2(n):

    if n < 1:
        print('您的输入有误.')
        return -1

    if n ==1 or n == 2:
        return 1
    else:
        return Fibonacci2(n - 1) + Fibonacci2(n - 2)


n = int(input('请输入月数:'))
result = Fibonacci2(n)
if result != -1:
    print('%d个月后共有%d只兔子.'%(n,Fibonacci2(n)))

'''

#汉诺塔

'''

import time

def Hanoi(n,x,y,z):
    
    if n == 1:
        print(x,'-->',z)

    else:
        Hanoi(n-1,x,z,y)    #将前n-1个盘子从x->y
        print(x,'-->',z)    #将最底下的最后一个盘子移动到z
        Hanoi(n-1,y,x,z)    #将y上的n-1个盘子移动到z

n = int(input('请输入汉诺塔的层数:'))
t1 = time.monotonic()
Hanoi(n,'X','Y','Z')
t2 = time.monotonic()
print('运行时间:',t2-t1)

'''





















    

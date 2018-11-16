# 花式编程


# 7：判断吉祥数

'''
from random import randrange
import sys
sys.setrecursionlimit(1000000)

def checkLucky1(num):
    #递归法
    if num == 0:
        return False
    quotient, lastDigit = divmod(num, 10)
    if lastDigit == 8:
        return True
    return checkLucky1(quotient)

def checkLucky2(num):
    return '8' in str(num)

for _ in range(1000000):
    num = randrange(10**80)
    if checkLucky1(num) != checkLucky2(num):
        print(num)

'''
        
# 3

'''
from random import randrange

print('20个数的随机列表为:',end='')
lst = [randrange(10) for _ in range(20)]
print(lst)

print('删除列表中所以的奇数后为:',end='')
lst = list(filter(lambda x: x%2==0, lst))
print(lst)


print('20个数的随机列表为:',end='')
lst = [randrange(10) for _ in range(20)]
print(lst)

print('偶数位置上的元素降序排列，奇数位置上的元素不变:',end='')
lst[::2] = sorted(lst[::2], reverse=True)
print(lst)

'''



# 4 把以整数列表，奇数放后面，偶数放前面


from random import randrange

def demo1(intList):
    return sorted(intList,\
                  key=lambda item:item%2==0)


print('20个数的随机列表为:',end='')
lst = [randrange(10) for _ in range(20)]
print(lst)

lst = demo1(lst)
print(lst)


def demo2(intList):
    odd = []
    even = []
    for item in intList:
        if item%2:
            odd.append(item)
        else:
            even.append(item)
    return odd + even

print('20个数的随机列表为:',end='')
lst = [randrange(10) for _ in range(20)]
print(lst)

lst = demo2(lst)
print(lst)


















































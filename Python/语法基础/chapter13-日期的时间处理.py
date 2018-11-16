
#例1
'''
from time import *
strftime("%c",localtime())
strftime("%Y年%m月%d日%H时%M分%S秒",localtime())

'''
#例2

'''
import time

def test():
    sum = 0
    for i in range(0,9999999):
        sum+=i
    return sum

if __name__ == '__main__':
    t1=time.monotonic()
    print(test())
    t2=time.monotonic()
    print('运行时间:',t2-t1)

'''

#例3






'''
import time
import random
import threading

# 自定义生产者线程类

class Producer(threading.Thread):
    
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global eventEmpty, eventFull
        # 根据Event对象是否已经做出设置做出不同的响应
        while True:
            # 随机等待0-4秒
            time.sleep(random.randrange(5))
            # 缓冲区满则等待
            if eventFull.isSet():
                print('Producer is writing....')
                # 消费者等待完
                eventEmpty.wait()
            # 开始生产
            print("Producing...", end='')
            for i in range(10):
                lst.append(i)
                print(i, end=' ')
            print()
            # 清除"空"标记
            eventFull.clear()
            # 通知消费者可以消费
            eventFull.set()


class Consumer(threading.Thread):

    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global eventEmpty, eventFull
        # 根据Event对象是否已设置做出不同的响应
        while True:
            # 随机等待0-4秒
            time.sleep(random.randrange(5))
            # 缓冲区空则等待
            if eventEmpty.isSet():
                print("Consumer is waiting....")
                # 等待生产者生产
                eventFull.wait()
            # 开始消费
            print("Consuming....", end='')

            for i in lst:
                print(i, end=' ')
            print()
            # 清空缓冲区
            lst.clear()
            # 通知消费完
            eventFull.clear()
            # 通知生产者可以生产
            eventEmpty.set()


lst = []
eventFull  = threading.Event()
eventEmpty = threading.Event()
# 设置标志
eventEmpty.set()

Producer('Producer').start()
Consumer('Consumer').start()
            
'''

# 例二

import threading
import time
import random


'''
def Demo(start, end):
    for i in range(start, end):
        print(i)

t = threading.Thread(target = Demo, args=(1,10))
t.start()

'''

class MyThreading(threading.Thread):

    def __init__(self, begin, end):
        threading.Thread.__init__(self)
        self.begin = begin
        self.end   = end

    def run(self):
        for i in range(self.begin, self.end):
            print('waiting...')
            time.sleep(random.randrange(5))
            print(i)

t = MyThreading(1,10)
t.start()









            











            

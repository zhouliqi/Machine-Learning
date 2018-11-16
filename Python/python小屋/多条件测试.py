# 问题描述：输入一个包含若干个整数的列表，
# 如果列表中的所有数字都大于5就输出字符串ALL
# 如果有多于一半的数字大于5，输出字符串HALF
# 如果所有数字都不大于5，输出字符串NO

import time
def test1(numbers):
    start = time.time()
    times = 0
    for num in numbers:
        if num > 5:
                    times += 1
    length = len(numbers)
    if times == length:
        print('ALL')
    elif times > length/2:
        print('HALF')
    elif times == 0:
        print('NO')
    end = time.time()
    print("运行时间为：", (end - start))
    
def test2(numbers):
    start = time.time()
    # 生成器表达式，统计大于5的数字的个数
    times = sum(1 for num in numbers if num > 5)
    length = len(numbers)
    if times == length:
        print('ALL')
    elif times > length/2:
        print('HALF')
    elif times == 0:
        print('NO')
    end = time.time()
    print("运行时间为：", (end - start))

def test3(numbers):
    start = time.time()
    # 列表推导式+count方法，统计大于5的数字的个数
    times = [num > 5 for num in numbers].count(True)
    length = len(numbers)
    if times == length:
        print('ALL')
    elif times > length/2:
        print('HALF')
    elif times == 0:
        print('NO')
    end = time.time()
    print("运行时间为：", (end - start))

def test4(numbers):
    start = time.time()
    conditions = [num > 5 for num in numbers]
    if all(conditions):
        print('ALL')
    elif conditions.count(True) / len(conditions) > 0.5:
        print('HALF')
    elif not any(conditions):
        print('NO')
    end = time.time()
    print("运行时间为：", (end - start))
    
    
numbers = eval(input("请输入一个包含若干个整数的列表:"))
test1(numbers)
test2(numbers)
test3(numbers)
test4(numbers)



























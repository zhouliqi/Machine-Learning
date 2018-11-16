#------------------2.8类的声明，对象的创建和调用----------
"""
class Person:
	def sayhello(self):
		print("Hello World!")
		print("How are you!")
p=Person()
p.sayhello()
print('\n')

"""

#------------------2.9.1函数的声明和调用------------------
"""

def sayhello():
        print('What is your question?')
        print("The answer is : ",end='')
        print('To be or not to be , this is a question!')
sayhello()
print('\n')

"""

#------------------2.9.4输入和输出函数---------------------
"""

import datetime
yourname=input("请输入您的姓名：")
birthyear=int(input("请输入您的出生年份："))
age=datetime.date.today().year-birthyear
print("您好{0}.您今年{1}岁.".format(yourname,age))

"""

#------------------2.9.4输入和输出函数---------------------
"""

import getpass
def checkuser(user,passwd):
        if user=='zhouliqi' and passwd=='158319927':
                return True
        else:
                return False

if True: #_name_=='_main_':
        user=input('用户名：')
        passwd=getpass.getpass('密码：')
        if checkuser(user,passwd):
                print("登录成功")
        else:
                print("登录失败，您的用户名或密码有误")

"""

#---------------------------------------

"""

def getvalue(b,r,n):
        total=b*(1+r)**n
        return total
b=float(input("请输入本金："))
r=float(input("请输入年利率："))
n=int(input("请输入年份："))
total=getvalue(b,r,n)
print('本金利率和为：{0:.2f}'.format(total))      #保留小数点后两位

"""      

#---------------------------------------
'''
import random
import datetime

quote = ['只问执着，无问西东!',\
         '一个人若生活得诚恳，他一定是生活在一个遥远的地方。',\
         '遗憾千万种，各人皆不同',\
         '从小我就懂得保护自己，我知道要想不被人拒绝，最好的办法就是先拒绝别人',\
         '我曾经听人说过，当你不可以再拥有的时候。你唯一可以做的，就是让自己不要忘记',\
         ]

print("电脑：你好啊！")
print("电脑：你叫什么,答对了才能为你服务喔：")
name=input("你：")
if (name!="周立齐"):
        print("电脑：您不是这台电脑的主人喔！")

else:
        print('电脑：今天是',datetime.date.today())
        print('电脑：你好，小周，今天的语录是---',random.choices(quote))
        print("电脑：您好，你想要我做什么呢？")
        print("电脑：你想要我夸你嘛？yes or no：")
        echo=input("你：")
        if(echo=='no'):
                print("电脑：算了，今天先不夸你了.")
        else:
                print("电脑：我好中意你呀.")

        print("电脑：你想查看今天的幸运数字嘛？yes or no：")
        look=input("你：")
        if(look=='no'):
                print("电脑：今天不看幸运数字.")
        else:
                print("电脑：您今天的幸运随机数是：",random.choice(range(10)))

        
        print('好了，爱你，挂了，下次再约')
'''
from sklearn.datasets import fetch_lfw_people
from sklearn import datasets
'''faces = fetch_lfw_people(min_faces_per_person=60)
print(faces.target_names)
print(faces.images.shape)'''
print(datasets.get_data_home())















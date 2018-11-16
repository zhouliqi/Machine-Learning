#例9-1
'''
class Person1:
    pass
p1=Person1()
print(type(p1))
'''
#例9-2
'''
class Person2:
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
    def say_hi(self):
        print('您好，我叫{0},今年{1}岁，我的电话是{2}'.format(self.name,self.age,self.tel))
p1=Person2('周立齐',20,'18296316787')
p1.say_hi()

'''

#例9-3
'''

class Person3:
    count=0
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
        Person3.count+=1
    def __del__(self):
        Person3.count-=1
    def say_hi(self):
        print('您好，我叫{0},今年{1}岁，我的电话是{2}'.format(self.name,self.age,self.tel))
    def get_count():
        print('总计数为:',Person3.count)
print('总计数为:',Person3.count)
p31=Person3('周立齐',20,'18296316787')
p31.say_hi()
Person3.get_count()
p32=Person3('占雄',20,'13698086817')
p32.say_hi()
Person3.get_count()
del p31
Person3.get_count()
del p32
Person3.get_count()

'''

#例9-4
'''
class Person11:
    def __init__(self,name):
        self.__name=name
    @property
    def name(self):
        """ I'm the 'x' property."""
        return self.__name
    
#测试代码
if __name__== '__main__':

    p=Person11('周立齐')
    print(p.name)

'''
#例9-11
'''

class TemperatureConverter:
    
    @classmethod
    def c2f(cls,t_c):       #摄氏温度到华氏温度的转换
        t_c=float(t_c)
        t_f=(t_c*9/5)+32
        return t_f
    
    @classmethod
    def cf2(cls,t_f):
        t_f=float(t_f)
        t_c=(t_f-32)*5/9
        return t_c

    #测试代码
if __name__=='__main__':
        
    print('1:从摄氏温度到华氏温度.')
    print('2:从华氏温度到摄氏温度.')
    choice=int(input('请输入您的选择：'))
    if choice==1:
        t_c=float(input('请输入摄氏温度：'))
        t_f=TemperatureConverter.c2f(t_c)
        print("华氏温度为：{0:.2f}".format(t_f))
        
    elif choice==2:
        t_f=float(input('请输入华氏温度：'))
        t_c=TemperatureConverter.cf2(t_f)
        print("摄氏温度为：{0:.2f}".format(t_c))

    else:
            print("无此选项.")
            
'''


#例9-12
'''
class Book:
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price
    def __check_name(self):
        if self.name=='':
            return False
        else:
            return True
    def get_name(self):
        if self.__check_name():
            print(self.name,self.author)
        else:
            print('No Value')
b=Book("Python程序设计","小周",1.0)
b.get_name()

'''
    
#例9-19
'''
from math import pi

class Dimension:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        pass
class Circle(Dimension):
    def __init__(self,r):
        Dimension.__init__(self,r,0)
    def area(self):
        return pi*self.x*self.x
class Rectangle(Dimension):
    def __init(self,w,h):
        Dimension.__init__(self,w,h)
    def area(self):
        return self.x*self.y
d1=Circle(2.0)
d2=Rectangle(2.0,4.0)
print('圆的面积为{0:.2f},矩形的面积为{1:.2f}'.format(d1.area(),d2.area()))

'''

        


















        



#思考题

'''     #第3题

class parent:
    def __init__(self,param):
        self.v1=param
class child(parent):
    def __init__(self,param):
        parent.__init__(self,param)
        self.v2=param

obj=child(100);
print("%d %d"%(obj.v1,obj.v2))


'''
'''      #第四题

class Amount:
    def __init__(self,id):
        self.id=id
        id=888
acc=Amount(100)
print(acc.id)

'''
'''     #第五题

class amount:
    def __init__(self,id,balance):
        self.id=id
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
acc1=amount('1234',100)
acc1.deposit(500)
acc1.withdraw(200)
print(acc1.balance)

'''
#第六题
'''
class A:
    def __init__(self,a,b,c):
        self.x=a+b+c
a=A(1,2,3)
b=getattr(a,'x')
setattr(a,'x',b+1)
print(a.x)

'''

#第七题
'''
d1={'a':[1,2],'b':2}
d2=d1.copy()
d1['a'][0]=6
sum=d1['a'][0]+d2['a'][0]
print(sum)

'''
#第八题
'''

from copy import *
d1={'a':[1,2],'b':2}
d2=deepcopy(d1)
d1['a'][0]=6
sum=d1['a'][0]+d2['a'][0]
print(sum)

'''
#第十一题
'''

class Person:
    def __init__(self,id):
        self.id=id
mary=Person(123)
mary.__dict__['age']=18
mary.__dict__['gender']='female'
print(mary.age+len(mary.__dict__))

'''






























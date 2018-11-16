#================================================

'''

item_counter={}
def addone(item):
    if item in item_counter:
        item_counter[item]+=1
    else:
        item_counter[item]=1
addone('Apple');addone('Pear');addone('apple')
addone('Apple');addone('Kiwi');addone('apple')
print(item_counter)

'''

#================================================

'''

numbers={}
numbers[(1,2,3)]=1
numbers[(2,1)]=2
numbers[(1,2)]=3
sum=0
for k in numbers:
    sum+=numbers[k]
print(len(numbers),'',sum,'',numbers)

'''

#================================================

'''

d1={'a':1,'b':2};d2=d1;d1['a']=6;           # d2=d1这条语句是指d2引用d1
sum=d1['a']+d2['a']
print(sum)

'''

#================================================

'''
d1={'a':1,'b':2};                   # d2=dict(d1)这条语句是指将d1的内容赋值给d2
d2=dict(d1);d1['a']=6; 
sum=d1['a']+d2['a']
print(sum)

'''
#================================================

'''

week={1:'Mon',2:'Tues',3:'Wed',4:'Thur',4:'Fir',6:'Sat',7:'Sun'}
for k in week.keys():
    print(k,end=' ')
print()
for i in week.values():
    print(i,end='  ')
print()
for item in week.items():
        print(item,end=' ')

'''


#================================================






























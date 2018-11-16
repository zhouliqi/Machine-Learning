#=============1：随机生成一副扑克牌====================

"""

from random import *
cards=['梅花2','梅花3','梅花4','梅花5','梅花6','梅花7','梅花8','梅花9','梅花10','梅花J','梅花Q','梅花K','梅花A',
       '方块2','方块3','方块4','方块5','方块6','方块7','方块8','方块9','方块10','方块J','方块Q','方块K','方块A',
       '红桃2','红桃3','红桃4','红桃5','红桃6','红桃7','红桃8','红桃9','红桃10','红桃J','红桃Q','红桃K','红桃A',
       '黑桃2','黑桃3','黑桃4','黑桃5','黑桃6','黑桃7','黑桃8','黑桃9','黑桃10','黑桃J','黑桃Q','黑桃K','黑桃A',
       ]
shuffle(cards)
deck1=[];deck2=[];deck3=[];deck4=[]
for i in range(13):
    deck1.append(cards.pop())
    deck2.append(cards.pop())
    deck3.append(cards.pop())
    deck4.append(cards.pop())
print(deck1);print(deck2);print(deck3);print(deck4);

"""

#=============2：====================
item_counter={}
def addone(item):
    if item in item_counter:
        item_counter[item]+=1
    else:
        item_counter[item]=1
addone('Apple');addone('Pear');addone('apple')
addone('Apple');addone('Kiwi');addone('apple')
print(item_counter)

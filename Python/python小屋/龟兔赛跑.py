# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 22:32:13 2018

@author: 小周

"""
'''
=======================
绘制龟兔赛跑现场
=======================
'''
from turtle import Turtle, ontimer, mainloop

rabbit = Turtle()
rabbit.hideturtle()
rabbit.shape('turtle')
rabbit.up()
rabbit.back(300)
rabbit.left(50)
rabbit.showturtle()
rabbit.down()

def rabbitMove():
    if usedTime < 50:       # 奔跑
        rabbit.forward(3)
    elif usedTime < 550:    # 睡觉,位移不变
        rabbit.setheading(0)
        rabbit.forward(0.5)
    else:                   # 追赶 
        rabbit.setheading(50)
        rabbit.forward(4)
        
tortoise = Turtle()
tortoise.hideturtle()
tortoise.shape('turtle')
tortoise.color(0.3, 0.6, 0.4)
tortoise.pensize(3)
tortoise.up()
tortoise.back(300)
tortoise.left(30)
tortoise.showturtle()
tortoise.down()

def tortoiseMove():
    tortoise.forward(1) # 乌龟一直匀速爬行
    
usedTime = 0
def move():
    global usedTime
    
    rabbitPosition = rabbit.ycor()
    tortoisePosition = tortoise.ycor()
    if max(rabbitPosition, tortoisePosition) > 300:
        write = Turtle()
        write.hideturtle()
        if rabbitPosition > 300:
            msg = 'Rabbit win!'
        else:
            msg = 'Tortoise win!'
        write.write(msg, align='center', font=('simfang', 30, 'bold'))
    else:
        rabbitMove()
        tortoiseMove()
        ontimer(move, 100)
        usedTime = usedTime + 1

ontimer(move, 100)
mainloop()













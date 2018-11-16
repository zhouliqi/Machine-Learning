
#画一个爱心

'''

from turtle import *
def curvemove():
    for i in range(200):
        right(1)
        forward(1)
color('red','pink')        
begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()
done()

'''


#画两个爱心

'''

from turtle import *
from time import sleep

def go_to(x, y):
   up()
   goto(x, y)
   down()


def big_Circle(size):  #函数用于绘制心的大圆
   speed(10)
   for i in range(150):
       forward(size)
       right(0.3)

def small_Circle(size):  #函数用于绘制心的小圆
   speed(10)
   for i in range(210):
       forward(size)
       right(0.786)

def line(size):
   speed(1)
   forward(51*size)

def heart( x, y, size):
   go_to(x, y)
   left(150)
   begin_fill()
   line(size)
   big_Circle(size)
   small_Circle(size)
   left(120)
   small_Circle(size)
   big_Circle(size)
   line(size)
   end_fill()

def arrow():
   pensize(10)
   setheading(0)
   go_to(-400, 0)
   left(15)
   forward(150)
   go_to(339, 178)
   forward(150)

def arrowHead():
   pensize(1)
   speed(5)
   color('red', 'red')
   begin_fill()
   left(120)
   forward(20)
   right(150)
   forward(35)
   right(120)
   forward(35)
   right(150)
   forward(20)
   end_fill()


def main():
   pensize(2)
   color('red', 'pink')
   #getscreen().tracer(30, 0) #取消注释后，快速显示图案
   heart(200, 0, 1)          #画出第一颗心，前面两个参数控制心的位置，函数最后一个参数可控制心的大小
   setheading(0)             #使画笔的方向朝向x轴正方向
   heart(-80, -100, 1.5)     #画出第二颗心
   arrow()                   #画出穿过两颗心的直线
   arrowHead()               #画出箭的箭头
   go_to(400, -300)
   write("", move=True, align="left", font=("宋体", 30, "normal"))
   done()

main()

'''


#画一条五彩蛇

'''

import turtle

def drawSnake(rad,angle,len,neckrad):
        mycolor=["black","red","red","blue","yellow"]
        yocolor=["yellow","green","yellow","red","red"]
        for i in range(len):
            turtle.pencolor(mycolor[i])
            turtle.circle(rad,angle)
            turtle.pencolor(yocolor[i])
            turtle.circle(-rad,angle)
        turtle.pencolor("green")
        turtle.circle(rad,angle/2)
        turtle.pencolor("yellow")
        turtle.fd(rad)
        turtle.pencolor("red")
        turtle.circle(neckrad+1,180)
        turtle.pencolor("green")
        turtle.fd(rad*2/3)

def main():
       turtle.setup(1300,800,0,0)
       pythonsize=30
       turtle.pensize(pythonsize)
       turtle.seth(-40)
       drawSnake(40,80,5,pythonsize/2)


main()

'''



#爱心

'''

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,2*np.pi, 0.1)
x = 16*np.sin(t)**3
y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
plt.plot(x,y,color = 'red')
plt.show()

'''

'''
import turtle
#turtle.screensize(800,600, "green")
turtle.setup(width=0.4,height=0.6)

'''

#画一条蟒蛇

'''

import turtle

def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor("green")
    turtle.seth(-40)
    drawSnake(40,80,5,pythonsize/2)

main()

'''



























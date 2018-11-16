# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:59:50 2018

@author: 小周

"""

'''
==========================================
python+turtle交互式绘图：可以用鼠标拖动的小海龟
==========================================
'''

from turtle import Screen, Turtle, mainloop 

class ColorTurtle(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape("turtle") # 画笔形状
        self.resizemode("user")
        self.shapesize(3, 3, 0) # 小海龟的大小
        self.pensize(10) # 画笔粗细
        self._color = [0, 0, 0]
        self.x = x
        self._color[x] = y
        self.color(self._color) # 画笔颜色
        self.speed(0) # 绘画速度,0表示最快
        self.left(90) # 向左旋转90度
        self.up()
        self.goto(x, 0) # 移动到指定位置
        self.down()     # 使用当前颜色绘制一条线
        self.sety(1)    # 移动到y坐标为1的位置,x坐标不变
        self.up()
        self.sety(y)    # 小海龟初始位置
        self.pencolor("black")  # 小海龟轮廓线的颜色
        self.ondrag(self.shift) # 设置鼠标拖动时间处理时间
        
    def shift(self, x, y):
        self.sety(max(0, min(y, 1))) # 限定小海龟y坐标在0到1之间
        self._color[self.x] = self.ycor() # 对小海龟当前y坐标设置填充色
        self.fillcolor(self._color) # 对小海龟进行填充
        setbgcolor() # 每次拖动小海龟之后重新设置窗口背景色
def setbgcolor():
    # 根据三个小海龟的当前位置设置窗口背景色
    screen.bgcolor(red.ycor(), green.ycor(), blue.ycor())

def main():
    global screen, red, green, blue
    screen = Screen()   # 返回窗口工作区对象
    screen.delay(0)     # 绘图无延迟
    screen.setworldcoordinates(-1, -0.3, 3, 1.3)

    red = ColorTurtle(0, .7)
    green = ColorTurtle(1, .3)
    blue = ColorTurtle(2, .6)
    setbgcolor()
    
    write = Turtle()
    write.hideturtle()
    write.up()
    write.goto(1, 1.15)
    write.write("Welcome to 小周 GAME!", align="center", font=("Arial", 30, ("bold", "italic")))
    

if __name__ == '__main__':
    main()
    mainloop()



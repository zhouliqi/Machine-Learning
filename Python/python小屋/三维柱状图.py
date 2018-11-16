# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:48:21 2018

@author: 小周

"""

# Python绘制每个柱的颜色各不相同的三维柱状图
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x = np.random.randint(0, 40, 10)
y = np.random.randint(0, 40, 10)
z = 80 * abs(np.sin(x + y))
ax = plt.subplot(projection='3d') # 三维图形

for xx, yy, zz in zip(x, y, z):
    color = np.random.random(3) # 随机颜色元祖
    ax.bar3d(xx,    # 每个柱的x坐标
             yy,    # 每个柱的y坐标
             0,     # 每个柱的起始z坐标
             dx=1,  # x方向的宽度
             dy=1,  # y方向的宽度
             dz=zz, # z方向的高度
             color=color) # 每个柱的颜色
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()


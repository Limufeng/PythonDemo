'''
Created on 2018年7月24日

@author: MF
'''
import turtle as t

# 初始位置
t.pu()
t.left(90)
t.fd(200)
t.pd()
t.right(90)

# 花蕊
t.fillcolor("red")
t.begin_fill()
t.circle(10, 180)
t.circle(25, 110)
t.left(50)
t.circle(60, 45)
t.circle(20, 170)
t.right(24)
t.fd(30)
t.left(10)
t.circle(30, 110)
t.fd(20)
t.left(40)
t.circle(90, 70)
t.circle(30, 150)
t.right(30)
t.fd(15)
t.circle(80, 90)
t.left(15)
t.fd(45)
t.right(165)
t.fd(20)
t.left(155)
t.circle(150, 80)
t.left(50)
t.circle(150, 90)
t.end_fill()

# 花瓣
t.left(150)
t.circle(-90, 70)
t.left(20)
t.circle(75, 105)
t.seth(60)
t.circle(80, 98)
t.circle(-90, 40)

# 花瓣
t.left(180)
t.circle(90, 40)
t.circle(-80, 98)
t.seth(-83)

# 叶子
t.fd(30)
t.left(90)
t.fd(25)
t.left(45)
t.fillcolor("green")
t.begin_fill()
t.circle(-80, 90)
t.right(90)
t.circle(-80, 90)
t.end_fill()

t.right(135)
t.fd(60)
t.left(180)
t.fd(85)
t.left(90)
t.fd(80)

# 叶子
t.right(90)
t.right(45)
t.fillcolor("green")
t.begin_fill()
t.circle(80, 90)
t.left(90)
t.circle(80, 90)
t.end_fill()

t.left(135)
t.fd(60)
t.left(180)
t.fd(60)
t.right(90)
t.circle(200, 60)
t.done()

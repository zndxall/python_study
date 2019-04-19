#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from turtle import *
import random
def draw_rectangle():  #画长方形
    width(4)#设置笔刷的宽度
    forward(250) #前进
    right(90) #右转90度
    pencolor('red') #笔刷颜色，笔刷颜色默认为黑色
    forward(100)
    right(90)
    pencolor('green')
    forward(250)
    right(90)
    pencolor('blue')
    forward(100)
    right(90)
    #done() #绘图完成后调用done()函数，让窗口进入消息循环，等待被关闭。否则窗口被立刻关闭
    reset() #清空画布，重置为初始状态

def drawStar(x,y): #画五角星
    pencolor("black")
    fillcolor("red")
    pensize(2)
    pu()
    goto(x,y)
    pd()
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

#画小彩环
def draw_ringcell():
    colormode(255)
    width(2)
    for n in range(200):
        r=int(random.uniform(0,255))
        g=int(random.uniform(0,255))
        b=int(random.uniform(0,255))
        fd(100)
        if(n%2==0):
            pencolor(r,g,b)
            rt(155)
        else:
            pencolor(r,g,b)
            lt(100)
    #done()
    reset()


def draw_tree(l, level):

    global r, g, b
    w = width()
    width(w * 3.0 / 4.0)
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l
    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)
    width(w)

#画小猪佩奇
def draw_peggi():
    screensize(400, 300)
    pensize(4)  # 设置画笔的大小
    colormode(255)  # 设置GBK颜色范围为0-255
    color((255, 155, 192), "pink")  # 设置画笔颜色和填充颜色(pink)
    setup(840, 500)  # 设置主窗口的大小为840*500
    speed(10)  # 设置画笔速度为10
    # 鼻子
    pu()  # 提笔
    goto(-100, 100)  # 画笔前往坐标(-100,100)
    pd()  # 下笔
    seth(-30)  # 笔的角度为-30°
    begin_fill()  # 外形填充的开始标志
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)  # 向左转3度
            fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()  # 依据轮廓填充
    pu()  # 提笔
    seth(90)  # 笔的角度为90度
    fd(25)  # 向前移动25
    seth(0)  # 转换画笔的角度为0
    fd(10)
    pd()
    pencolor(255, 155, 192)  # 设置画笔颜色
    seth(10)
    begin_fill()
    circle(5)  # 画一个半径为5的圆
    color(160, 82, 45)  # 设置画笔和填充颜色
    end_fill()
    pu()
    seth(0)
    fd(20)
    pd()
    pencolor(255, 155, 192)
    seth(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()
    # 头
    color((255, 155, 192), "pink")
    pu()
    seth(90)
    fd(41)
    seth(0)
    fd(0)
    pd()
    begin_fill()
    seth(180)
    circle(300, -30)  # 顺时针画一个半径为300,圆心角为30°的园
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    seth(161)
    circle(-300, 15)
    pu()
    goto(-100, 100)
    pd()
    seth(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)  # 向左转3度
            fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()
    # 耳朵
    color((255, 155, 192), "pink")
    pu()
    seth(90)
    fd(-7)
    seth(0)
    fd(70)
    pd()
    begin_fill()
    seth(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()
    pu()
    seth(90)
    fd(-12)
    seth(0)
    fd(30)
    pd()
    begin_fill()
    seth(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()
    # 眼睛
    color((255, 155, 192), "white")
    pu()
    seth(90)
    fd(-20)
    seth(0)
    fd(-95)
    pd()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    pu()
    seth(90)
    fd(12)
    seth(0)
    fd(-3)
    pd()
    begin_fill()
    circle(3)
    end_fill()
    color((255, 155, 192), "white")
    pu()
    seth(90)
    fd(-25)
    seth(0)
    fd(40)
    pd()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    pu()
    seth(90)
    fd(12)
    seth(0)
    fd(-3)
    pd()
    begin_fill()
    circle(3)
    end_fill()
    # 腮
    color((255, 155, 192))
    pu()
    seth(90)
    fd(-95)
    seth(0)
    fd(65)
    pd()
    begin_fill()
    circle(30)
    end_fill()
    # 嘴
    color(239, 69, 19)
    pu()
    seth(90)
    fd(15)
    seth(0)
    fd(-100)
    pd()
    seth(-80)
    circle(30, 40)
    circle(40, 80)
    # 身体
    color("red", (255, 99, 71))
    pu()
    seth(90)
    fd(-20)
    seth(0)
    fd(-78)
    pd()
    begin_fill()
    seth(-130)
    circle(100, 10)
    circle(300, 30)
    seth(0)
    fd(230)
    seth(90)
    circle(300, 30)
    circle(100, 3)
    color((255, 155, 192), (255, 100, 100))
    seth(-135)
    circle(-80, 63)
    circle(-150, 24)
    end_fill()
    # 手
    color((255, 155, 192))
    pu()
    seth(90)
    fd(-40)
    seth(0)
    fd(-27)
    pd()
    seth(-160)
    circle(300, 15)
    pu()
    seth(90)
    fd(15)
    seth(0)
    fd(0)
    pd()
    seth(-10)
    circle(-20, 90)
    pu()
    seth(90)
    fd(30)
    seth(0)
    fd(237)
    pd()
    seth(-20)
    circle(-300, 15)
    pu()
    seth(90)
    fd(20)
    seth(0)
    fd(0)
    pd()
    seth(-170)
    circle(20, 90)
    # 脚
    pensize(10)
    color((240, 128, 128))
    pu()
    seth(90)
    fd(-75)
    seth(0)
    fd(-180)
    pd()
    seth(-90)
    fd(40)
    seth(-180)
    color("black")
    pensize(15)
    fd(20)
    pensize(10)
    color((240, 128, 128))
    pu()
    seth(90)
    fd(40)
    seth(0)
    fd(90)
    pd()
    seth(-90)
    fd(40)
    seth(-180)
    color("black")
    pensize(15)
    fd(20)
    # 尾巴
    pensize(4)
    color((255, 155, 192))
    pu()
    seth(90)
    fd(70)
    seth(0)
    fd(95)
    pd()
    seth(0)
    circle(70, 20)
    circle(10, 330)
    circle(70, 30)


# 画时钟
from datetime import *

# 抬起画笔，向前运动一段距离放下
def Skip(step):
    penup()
    forward(step)
    pendown()


def mkHand(name, length):
    # 注册Turtle形状，建立表针Turtle
    reset()
    Skip(-length * 0.1)
    # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
    begin_poly()
    forward(length * 1.1)
    # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
    end_poly()
    # 返回最后记录的多边形。
    handForm = get_poly()
    register_shape(name, handForm)


def Init():
    global secHand, minHand, hurHand, printer
    # 重置Turtle指向北
    mode("logo")
    # 建立三个表针Turtle并初始化
    mkHand("secHand", 135)
    mkHand("minHand", 125)
    mkHand("hurHand", 90)
    secHand = Turtle()
    secHand.shape("secHand")
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
        # 建立输出文字Turtle
    printer = Turtle()
    # 隐藏画笔的turtle形状
    printer.hideturtle()
    printer.penup()


def SetupClock(radius):
    # 建立表的外框
    reset()
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            forward(20)
            Skip(-radius - 20)

            Skip(radius + 20)
            if i == 0:
                write(int(12), align="center", font=("Courier", 14, "bold"))
            elif i == 30:
                Skip(25)
                write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                Skip(-25)
            elif (i == 25 or i == 35):
                Skip(20)
                write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                Skip(-20)
            else:
                write(int(i / 5), align="center", font=("Courier", 14, "bold"))
            Skip(-radius - 20)
        else:
            dot(5)
            Skip(-radius)
        right(6)


def Week(t):
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]


def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s/%d/%d" % (y, m, d)


def Tick():
    # 绘制表针的动态显示
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    secHand.setheading(6 * second)
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)
    tracer(False)
    printer.forward(65)
    printer.write(Week(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.home()
    tracer(True)
    # 100ms后继续调用tick
    ontimer(Tick, 100)


def draw_clock():
    # 打开/关闭龟动画，并为更新图纸设置延迟。
    tracer(False)
    Init()
    SetupClock(160)
    tracer(True)
    Tick()
    mainloop()

if __name__ == "__main__":
    '''
    #画圆形，正放形，三角形都可以在这里控制，满足内角之和为360度
    pencolor('yellow')
    for m in range(360): 
        forward(2) #边长
        left(1)#旋转度数
    #done()
    reset()
    '''
    draw_rectangle() # 画正方形
    for x in range(0, 250, 50):  # 画五角星
        drawStar(x, 0)
    # done()
    reset()
    draw_ringcell()  # 画小彩环
   
    # 设置色彩模式为RGB
    colormode(255)
    lt(90)
    lv = 11
    s = 30
    width(lv)
    # 初始化RGB颜色
    r = g = b = 0
    pencolor(r, g, b)
    penup()
    l = 80
    bk(l)
    pendown()
    fd(l)
    speed(0)
    draw_tree(l, 4) #画树
    # done()
    reset()
    draw_peggi() # 画小猪佩奇
    reset()
    draw_clock() # 画时钟

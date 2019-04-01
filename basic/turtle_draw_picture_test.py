#/usr/bin/env python
#coding=utf-8
from turtle import *
#1.海龟绘图就是指挥海龟前进、转向，海龟移动的轨迹就是绘制的线条。要绘制一个长方形，只需要让海龟前进、右转90度，反复4次
#画长方形
width(4)#设置笔刷的宽度

#笔刷颜色默认为黑色
forward(250) #前进
right(90) #右转90度


pencolor('red') #笔刷颜色
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
        
for x in range(0,250,50):
    drawStar(x,0)
   
#done()
reset()

#画圆形，正放形，三角形都可以在这里控制，满足内角之和为360度
pencolor('yellow')
for m in range(360): 
    forward(2) #边长
    left(1)#旋转度数
#done()
reset()

#画小彩环
import random
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

  
#设置色彩模式为RGB
colormode(255)
lt(90)
lv=14
l=100
s=45
width(lv)

#初始化RGB颜色
r=0
g=0
b=0
pencolor(r,g,b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l,level):
    global r,g,b
    w=width()
    width(w * 3.0 / 4.0 )
    r=r+1
    g=g+2
    b=b+3
    pencolor(r % 200, g % 200, b % 200)
    
    l=3.0 / 4.0 * l
    lt(s)
    fd(l)
    
    if level < lv:
        draw_tree(l,level +1)
    bk(l)
    rt(2*s)
    fd(l)
        
    if level < lv:
        draw_tree(l,level +1)
    bk(l)
    lt(s)   
    width(w)
speed("faster")
draw_tree(l,4)
#done()
reset()

#画时钟
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
        write(int(i/5), align="center", font=("Courier", 14, "bold")) 
        Skip(-25) 
      elif (i == 25 or i == 35): 
        Skip(20) 
        write(int(i/5), align="center", font=("Courier", 14, "bold")) 
        Skip(-20) 
      else: 
        write(int(i/5), align="center", font=("Courier", 14, "bold")) 
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
   
draw_clock()
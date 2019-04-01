#!/usr/bin/env python 
#coding=utf-8

from types import MethodType
from enum import Enum,unique
import logging

logging.basicConfig(level=logging.INFO)

class Stu1(object): #类,如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
    def __init__(self,name,score):#init前后都是两条下划线，init和self是固定的
        self.name=name
        self.score=score
        
    def print_score(self):
        print('name/score:%s %s' %(self.name,self.score))

class Stu2(object):
    def __init__(self,name,age): #实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__name=name
        self.__age=age
    def print_age(self):
        print('name/age:%s %s' %(self.__name,self.__age))
        return self.__name,self.__age
    def set_age(self,age):
        if(0<=age<=110):
            self.__age=age
        else:
            raise  ValueError('bad input age')
            
class Stu3(Stu2): #继承Stu1类
    pass
        
class Animal(object):
    def __init__(self):
        name="Land Animal"
    def get_info(self,age):
        __slot__('age') #slot看不懂
        self.age=age
        print("age:%d" %(self.age))

class Weekday(Enum):
    pass 
def fun():
    pass
test1=Stu1('test1',60) #test1是一个实例
test1.print_score()

test2=Stu2('test2',12) 
test2.print_age()
test2.set_age(13)
test2.print_age()
test2.__age=14 #这样不能修改age的值
test2.print_age()

test3=Stu3("test3",17)
test3.print_age()


print(isinstance(test3,Stu3)) #判断一个变量是否是某个类型可以用isinstance()判断
print(isinstance(test3,Stu2)) #stu3继承了stu2,所以stu3的实例也有stu2的类型
print(isinstance(test2,Stu3)) #但是反过来不行

print("test3的数据类型：",type(test3)) #type获取数据类型，优先使用isinstance
print("abc的数据类型：",type('abc'))

print(hasattr(test2,'set_age')) #获取实例属性
print(hasattr(test1,'name'))
print("dir显示属性:",dir(test1))

cat=Animal()
cat.name='kitty'
print(cat.name)
#print(cat)
#出错，why cat.get_info=MethodType(get_info,cat)
#cat.get_info(2)

Month=Enum('Month',('Jan','Feb','Mar','Apr','May')) #枚举类型定义常量
print(Month.Jan.value) #可以使用Moth.Jan来使用变量，变量的值使用Month.Jan.value获取
logging.info(Month(1))

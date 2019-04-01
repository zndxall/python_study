#!/usr/bin/env python
#coding=utf-8
import sys
import zipfile
import shutil
import os #引入输入输出模块
import time #引入时间模块
import calendar#引入日历
import datetime
import test
import math
import utils #导入utils模块

print("参数名：",sys.argv)    
name='john'
age='12'
print ("除第一个字符外的字符是 " +name[1])
print("hello" + " " + name)
print (name * 2) #输出两次，*表示重复操作
print (name + " " + age + " years old")
utils.my_slice()
utils.my_iteration()
utils.list_gen()
utils.my_generator()
next(utils.my_generator())
utils.my_iterator()
f_a=abs #绝对值函数abs复制给变量f_a
print("abs add result:",utils.add_num(-8,-5,f_a))
utils.map_num()
utils.str2int()
utils.my_filter()
utils.partial_fun()
utils.basic_fun(3,4)
print("add str1 and str2:",utils.andstr('happy ','day'))
utils.fun_time()

""" 多行注释用三个双引号
input_name=input("please input a name:")
print("user input name is :",input_name)
test.test1()
reload(test)
"""
rname=r'''hello
helen'''
print ("rname:",rname)
print('%2d-%02d' %(1,3))
print('%.2f' % 3.1415926)
L_P = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
lp1=L_P[2]
print(lp1[2])
#print(L_P[2,2])
print("hex(123):",hex(123))
utils.errorll('helen','M')
utils.errorll('Tom','G',11)
utils.errorll('Jim','A',13,'Shanghai')
utils.errorll('Kate','G',city='Xiamen')
utils.errorll('Selina','D',age=12)
utils.files_do()
print("add_end result:",utils.add_end([1,2,3]))
print("cacl1 result:",utils.cacl1((1,2,3))) #或者utils.cacl1([1,2,3])
print("cacl2 result:",utils.cacl2(1,2,3))
print("cacl2 result:",utils.cacl2(1))
list_c2=[1,2,3]
print("cacl2 result:",utils.cacl2(*list_c2))
#utils.person('test1',11)
utils.person('test2',12,grade='A',city='Beijing')
extal={'grade':'M','city':'Shanghai','school':'school1'}
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
#对kw的改动不会影响到函数外的extra
utils.person('test2',13,**extal)
utils.person1('test3',13,city='shanghai',job='student')
utils.person3('test4',14,job='student')
utils.files_do()
utils.memory_do()
utils.operate_file_or_dir()
utils.my_dumps()
utils.my_datetime()
utils.volid_string()


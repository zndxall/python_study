#!/usr/bin/evn python
#coding=utf-8

'utils.py'
_author_='Helen Ao'

import sys
import zipfile
import shutil
import os #引入输入输出模块
import time #引入时间模块
import calendar#引入日历
from datetime  import datetime
from collections import Iterable
from collections import Iterator
from functools import reduce
import functools
from io import StringIO #在内存中读写数据(str)
from io import BytesIO #在内存中读写数据(byte)
import pickle #序列化
import json #序列化
import re #正则匹配

def basic_fun(num1,num2): #基础功能
    print("判断：if-elif-elif-else,另外python中没有switch-case")
    if (num1 > num2):
        print ("less")
    else:
        print("big")
    print(num1==num2)
    print("==============循环=============")
    sum=0
    while num1 <= num2:
        sum=sum+num1
        num1+=1	
    print("sum:%d" %(sum))

#++++++++++++++++++++++++++++++++++函数+++++++++++++++++++++++++++++++++++++
def andstr(str1,str2): #检查参数类型

    #print(str1+str2)
    if not (isinstance(str1,str)):
       raise TypeError("bad str1 type")
    #return (str1,str ) 函数使用类似方法返回多个值
    return (str1+str2)
    
def donothing(): #pass空语句
    pass #pass是空语句，不做任何事情，一般用作站位语句，是为了保持程序结构的完整性
    
def fun_time():#时间和日历
    ticks=time.time()
    print("时间戳：",ticks)
    l_time = time.localtime(time.time())
    print("本地时间：",l_time)
    form_time=time.asctime(l_time)
    print("格式化时间：",form_time)
    #格式化为2016-03-20 11:45:32的形式
    form_t1=time.strftime("%Y-%m-%d %H:%M:%S",l_time)
    print("转换形式1：",form_t1)
    #格式化为sat mar 28 22:44:24 2016
    form_t2=time.strftime("%a %b %d %H:%M:%S %Y")
    print("转换形式2：",form_t2)
    cal=calendar.month(2018,6)
    print("2018年6月份的日历：",cal)
 
def my_datetime():
    now_time=datetime.now()
    print("current time：",now_time)
    ts_time=now_time.timestamp()
    print("对应时间戳：",ts_time)
    t_time=datetime.fromtimestamp(ts_time)
    print("时间戳转化成时间：",t_time)
    print("时间戳转化成utc时间：",datetime.utcfromtimestamp(ts_time))
    str_time='2015-6-1 18:11:40'
    print("str转化成时间：",datetime.strptime(str_time,'%Y-%m-%d %H:%M:%S'))
    print("时间转换成str:",now_time.strftime('%a,%b %d %Y-%m-%d %H:%M'))
    
    
def errorll(name,grand,age=7,city='Beijing'): #默认参数
#age和city就是默认参数，name和grand是必选参数
    print("name,grand,age,city:",name,grand,age,city)  
    
def add_end(L=None):#默认参数必须指向不变对象
#None就是不变对象，否则本次将会记住上次的执行结果
    if L is None:
        L=[]
    L.append('END')
    return L 
    
def cacl1(numbers): #可变参数
#调用的时候，需要先组装出一个list或tuple
    sum=0
    for n in numbers:
        sum=sum+1*n
    return sum
    
def cacl2(*numbers):#可变参数
    sum=0
    for n in numbers:
        sum=sum+2*n
    return sum   
    
def person(name,age,**kw):#关键字参数
    if 'city' in kw:
        #有city参数
        pass
    print("name:",name,"age:",age,"other:",kw)  
    
def person1(name,age,*,city,job):#命名关键字参数
#*后面指定了命名关键字参数,如果缺少*，city和job被认为是位置参数。
    print("name:",name,"age:",age,"city:",city,"job:",job)
    
def person2(name,age,*test,city,job):#命名关键字参数
#如果函数参数中已经有一个可变参数，那么就不在需要后面再加*
    print("name:",name,"age:",age,"city:",city,"job:",job,"test:",test)
    
def person3(name,age,*,city='Beijing',job):#命名关键字参数
#如果命名关键字参数已经有默认值，那么可以不传入改参数，比如city
    print("name:",name,"age:",age,"city:",city,"job:",job)
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的   


#++++++++++++++++++++++++++++++++++高级特性++++++++++++++++++++++++++++++++++++++++++++++++
def my_slice():# 切片
    print("-----------列表、元祖、字符串截取---------")
    L_sa=list(range(20))  
    print("列表：",L_sa)
    print("列表第一个元素: ",L_sa[0])
    print("列表倒数第一个元素: ",L_sa[-1])
    print("列表前4个元素: ",L_sa[0:4]) #等价于L_sa[:4],当索引从0开始时，0可以省略
    print("列表前十个每两个取一个: ",L_sa[:10:2])
    print("列表所有元素每四个取一个：",L_sa[::4])
    T_sa=tuple(range(20))
    print("元祖也是一种列表，区别是唯一不可变，也可以仿照列表做切片操作")
    print("元祖:",T_sa)
    print("元祖前4个元素: ",T_sa[0:4])
    print("字符串也可以当作列表，同样可以对字符串操作")
    S_str='ASFGDSKHL'
    print("字符串：",S_str)
    print("前两个字符：",S_str[:2])
    print("间隔三个取一个字符：",S_str[::3])
    print("字串串的长度：",len(S_str))
    print("丢掉首尾字符：",S_str[1:len(S_str)-1])

def my_iteration():#迭代   
#使用for .... in 实现
    print("=================字典===============")
    tinydict = {'A':'a1','B':'b1','C':'c1','D':'d1'}
    print("键值对：",tinydict.keys(),tinydict.values())
    #判断某个key是否存在于字典中，使用in 或者get()
    print("字典中是否存在hele(get):",tinydict.get('a1'))
    print("字典中是否存在hele(in):",'b1' in tinydict)
    print("判断字典是否可以迭代：",isinstance(tinydict,Iterable))
    print("字典默认迭代key：")
    for key in tinydict: 
        print("key:",key)
    print("迭代value：")
    for value in tinydict.values(): 
        print("value:",value)
    print("迭代key和value：")
    for k,v in tinydict.items(): 
        print("key:",key,"value:",value)
    print("迭代也可以处理字符串：")
    for ch in 'ASD':
        print("字符：",ch)
    print("Python内置的enumerate函数可以把一个list变成索引-元素对:")
    for i,value in enumerate(range(20,30)): #range(20,30)是一个列表生成式
        print("key","value:",i,value)
    print("其他使用：")
    for x,y in [(2,'t2'),(3,'t3'),(4,'t4')]:
        print("x->y:",x,y)

def list_gen():#列表生成式
    print("range生成列表：",list(range(30,40)))
    print("x*x resutl:",[x*x for x in range(1,10)])
    print("显示当前目录下的文件：",[cur_f for cur_f in os.listdir('.')])
    print("讲列表中的字符串全部转换成小写：",[myl.lower() for myl in ['Test1','TEST2']])

def my_generator():#生成器
    gen1=(x*x for x in range(1,5))
    for g1 in gen1:
        print(g1)
    print("step1:")
    yield 1
    print("step2:")
    yield (3)
    print("step3")
    yield (5)
 
def my_iterator():#迭代器
    print("bool value:",isinstance((x for x in range(5)),Iterator))
    print("bool value:",isinstance({},Iterator))
    print("bool value:",isinstance([],Iterator))
    print("bool value:",isinstance('abc',Iterator))
    print("-----使用iter()函数后的布尔值------------")
    print("bool value:",isinstance(iter({}),Iterator))
    print("bool value:",isinstance(iter([]),Iterator))
    print("bool value:",isinstance(iter('abc'),Iterator))
    
#++++++++++++++++++++++++++++++++++高阶函数：map,reduce,filter,sorted,lambda,装饰器，偏函数++++++++++++++++++++++++++++++++++++++++++++   
def add_num(x,y,f):
    return f(x)+f(y)

def map_num(): #map
    mr=map(lambda x:x*x,[1,2,3,4,5])  #使用匿名函数lambda构造简单的函数
    print("mr 列表：",list(mr))
    print("数字转换成字符：",list(map(str,[1,2,3,4])))
    
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
    
def str2int(): #reduce
    print("reduce and map result:",reduce(lambda x,y:x+y,map(char2num,'123456'))) #装换成int并相加
    
def my_filter(): #filter
    def is_odd(n):
        return n%2==1 #删除偶数，保留基数
    print("删除偶数，保留基数：",list(filter(is_odd,list(range(1,20)))))
    print("匿名函数改造：",list(filter(lambda n:n%2==1,list(range(1,20)))))
    def no_empty(ch):
        return ch and ch.strip()
    print("删除序列中的空字符：",list(filter(no_empty,['A','B',None,'C',' '])))

def partial_fun():#偏函数
    int2=functools.partial(int,base=2) #转换成二进制 (int 默认的base是10)
    print("转二进制：",int2('1000000'))
    max2=functools.partial(max,10)
    print("比10大的最大数：",max2(2,5,11,22))
    print("最大数：",max(5,2,4,11,8,30,16))

#+++++++++++++++++++++++++++++++++++++++IO编程++++++++++++++++++++++++++++++++++++++  
def files_do():# 文件处理
    src_empty_file = 'czt.txt'
    if hasattr(src_empty_file,'read'): #判读问价是否有可读属性
        print("can read") 
        # 创建一个空文件（不存在则创建）
    f = open(src_empty_file, 'w+')  
    f.write('Hello Helen')
    f.close()
    f1=open(src_empty_file, 'r+') 
    print(f1.read())
    f1.close()
    with open(src_empty_file,"a") as f:  #with会自动调用close函数，写的数据不会马上写入文件，必须调用close才能保证数据写入，所以使用with更加保险
        f.write("Happy Day!")
    f2=open(src_empty_file,'r')
    print(f2.read())
    f2.close()
    
def memory_do(): #内存的读写
    fs1=StringIO()
    fs1.write("test1")
    print(fs1.getvalue())
    fs2=StringIO('test2\ntest3\n')
    print(fs2.readline())
    #StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
    fb1=BytesIO()
    fb1.write('中文'.encode('utf-8')) #写入的不是str，而是经过UTF-8编码的bytes
    print(fb1.getvalue())
    fb2=BytesIO(b'\xe4')
    print(fb2.read())
    
def operate_file_or_dir():#操作文件和目录
    print("查看操作系统：",os.name) 
    if os.name == "nt":
        print("this is windows system")
    if os.name == "posix":
        print("this is linux or mac or unix system")
    #print("全部环境变量:",os.environ)
    print("环境变量PATH的值：",os.environ.get('PATH'))
    print("当前目录的绝对路径：",os.path.abspath('.'))
    cur_path=os.path.abspath('.')
    new_dir=os.path.join(cur_path,'testdir') #两个路径合并成一个路径用join
    if os.path.exists(new_dir): #判断文件夹是否存在,存在将返回True,存在就先删除再创建
        print("is exist and delete first")
        os.rmdir(new_dir)
    print("将创建新文件夹：",new_dir) #创建文件夹，第一步：要把文件夹的路径表示出来
    os.mkdir(new_dir) #第二步：创建文件夹
    if os.path.exists(new_dir):
        print("create success")
    print("把一个路径拆分成两个路径",os.path.split(new_dir)) #拆分用split,后一部分总是最后级别的目录或文件名
    cur_file=os.path.join(cur_path,'utils.py')
    print("获取文件后缀名:",os.path.splitext(cur_file)) #os.path.splitext(x)[1]获取第二部分（后缀），os.path.splitext(x)[0]获取第一部分[路径]
    #这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
    #os.rename('test.txt','test1.txt') #重命名文件
    #os.remove(test1.txt) #删除文件
    print("当前文件下的所有文件夹：",[x for x in os.listdir('.') if os.path.isdir(x)])
    print("当前路径下的所有python文件：",[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
 
class Stu(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

def dict2stu(d):
    return Stu(d['name'],d['age'],d['score'])

def my_dumps(): #序列化
    d_dict=dict(name='helen',age=18,score=90)
    fd=open('dump.txt','wb')
    pickle.dump(d_dict,fd) #序列化
    fd.close()
    fdr=open('dump.txt','rb')
    #print("序列化到文件中:",fdr.read())
    bk_d=pickle.load(fdr)
    print("反序列化：",bk_d)
    fdr.close()
    print("---------json序列化-------")
    print("json序列化：",json.dumps(d_dict))
    json_str='{"name":"Jim","age":17,"score":91}'
    print("json反序列化：",json.loads(json_str))
    print("-------高阶json:class序列化------")
    my_stu=Stu('Bob',17,91)
    print(json.dumps(my_stu,default=lambda obj:obj.__dict__)) #通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量
    #json.dumps不能直接序列化class,必须借助default参数转化
    print(json.loads(json_str,object_hook=dict2stu))
    
def volid_string(): #正则匹配，判断邮箱电话是否有效
    check_estring="010-12345"
    #下面的正则表示的是必须以三个数字开头（^\d{3}）,然后横线连接，再以三到八个数字结尾（-d{3,8}$）
    if re.match(r'^\d{3}\-\d{3,8}$',check_estring): 
        print("ok")
    else:
        print("wrong")



    
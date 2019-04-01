#!/usr/bin/env python

import os
from multiprocessing import Process,Queue #进程
from multiprocessing import Pool #进程池
import subprocess #子进程
import time
import threading #线程
import random

'''
# Only works on Unix/Linux/Mac:
pid=os.fork()
if pid == 0 :
    print("I am a kid process(%d) and my parent is %s " % (os.getpid(),os.getppid()))
else:
    print("i am parent process(%s) and  just create a kid process" %(os.getpid(),pid))
'''

#启动一个子进程执行并等待结束
def kid_run(name):
    print("Run child %s process %s" %(name,os.getpid()))
    
#如果要启动大量进程，可以使用pool的方式创建进程池
def long_time_task(name):
    print("child %s is running(proess %s) " %(name,os.getpid()))
    start=time.time()
    time.sleep(random.random())
    end=time.time()
    take_time=end - start
    print("Task %s use %0.2f " %(name,take_time))
 
#进程间通信，读和写
def my_write(q):
    print("wite process %s" %(os.getpid()))
    for value in ['A','B','C']:
        print("put %s to queue.."%value)
        q.put(value)
        time.sleep(10)

def my_read(q):
    print("read process %s" %(os.getpid()))
    while True:
        value=q.get(True)
        print("get %s from queue" %value)

def my_thread():
    print("thread %s is running...."%(threading.current_thread().name))
    for i in list(range(5)):
        print("list vale:",i)
    time.sleep(1)
    print("thread %s is end...."%(threading.current_thread().name))
   
balance=0 #当成余额
lock=threading.Lock()
def change_it(n):
    global balance 
    balance=balance+n #先存n元再取出来，结果应该还是0
    balance=balance-n
    
def run_thread(n):
    for i in range(1000000): #如果不加锁，这里执行次数太多，值就不对，存取数相同应该结果还是0才对
        lock.acquire()#先获取锁
        try:
            change_it(n)
        finally:
            lock.release() #改完后一定要记得释放锁

#创建全局ThreadLocal对象
#全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理,可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等
local_school=threading.local() 
  
def process_stu():  
    std=local_school.student
    print("student %s (in %s)" %(std,threading.current_thread().name))

def stu_thread(name):
    local_school.student=name# 绑定ThreadLocal的student
    process_stu()
        
if __name__=='__main__':
    print("Process parent %s start...." %(os.getpid()))
    pk1=Process(target=kid_run,args=('test',)) #创建子进程，传入一个函数和一个函数参数即可
    print("child process will start")
    pk1.start()
    pk1.join()
    print("child end")
      
    pk2=Pool(4)
    for i in range(5):
        pk2.apply_async(long_time_task,args=(i,))
    print("doing multiprocesse...")
    pk2.close()
    pk2.join()
    print("Pool Multiprocess done\n")
    
    print("$ ping www.baidu.com")
    sub_p1=subprocess.call(['ping','www.baidu.com']) #启动子进程，并控制输入输出
    print("Exit code:",sub_p1)
    
    print("$nslookup :") #进程需要输入配置时，使用communicate
    sub_p2=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output,err=sub_p2.communicate(b'set q=mx\nwww.google.com\nexit\n') #相当于设置set q=mx  www.google.com 
    print(output.decode('utf-8','ignore'))
    print("Exit code:\n",sub_p2.returncode)
    
    my_q=Queue()
    pw_k=Process(target=my_write,args=(my_q,))
    pr_k=Process(target=my_read,args=(my_q,))
    pw_k.start() #启动写入,并写入
    pr_k.start() #启动都出，并都出
    pw_k.join() #写结束后，关闭
    pr_k.terminate() #此处的读进程是死循环，要主动终止
    
    print("\n线程：")
    my_th1=threading.Thread(target=my_thread,name="newthread")
    my_th1.start()
    my_th1.join()
    print("thread %s is end...."%(threading.current_thread().name))
    
    print("\n多线程访问同一个全局变量时，需要加锁，否则执行次数多将会出错：") #
    my_th2=threading.Thread(target=run_thread,args=(5,))
    my_th3=threading.Thread(target=run_thread,args=(8,))
    my_th2.start()
    my_th3.start()
    my_th2.join()
    my_th3.join()
    print("余额：",balance)
    
    print("\n定义全局ThreadLocal:")
    my_th4=threading.Thread(target=stu_thread,args=('Amy',),name='Thread-A')
    my_th5=threading.Thread(target=stu_thread,args=('Bob',),name='Thread-B')
    my_th4.start()
    my_th5.start()
    my_th4.join()
    my_th5.join()
    
    

  
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
(多行注释使用三个英文的双引号)
产假计算器:
    产假计算工具（未考虑闰年），比如从五月某天开始，脚本后跟请假日期，如：sh Maternity_leave.sh 5.14
    基础产假98天+广东省增加产假80天，如遇难产/剖腹产增加30天
    使用说明：python Maternity_leave.py $day,$day 表示你的请假开始日期，比如5.12
"""

import sys
import time
from tkinter import *
#import tkinter as tk

def main():
    start_date=e1.get() # e1.get()是字符串，此处不能强制转换为int类型
    total_days=e3.get()
    total_days=int(total_days)
    if total_days != 178 and total_days !=208:
        print("请输入正确的休假天数")
        exit(1)
    #total_days=98 +80
    #cur_year=time.strftime("%Y",time.localtime(time.time()))
    cur_year=start_date.split(".")[0]
    cur_year=int(cur_year)
    print("start_day:",start_date,"total days:",total_days)
    start_day=start_date.split(".")[-1] #获取请假开始日期，比如5.14，那么开始日期就是14号
    start_day=int(start_day)
    small_month=[4,6,9,11]
    start_month=start_date.split(".")[1] #获取请假开始月份，比如5.14，那么开始月份就是5月
    start_month=int(start_month)
    if start_month > 12:
        print("pelase input right moth(<=12)")
        exit(1)
    if start_month in small_month and small_month != 1:
        if start_day > 30:
            print("%d is small month and please input right day( <=30)" %(start_month))
            exit(1)
        rest_day=30 - start_day + 1 #小月当月剩余天数（含请假当天）
    elif start_month==2:
        if start_day > 28:
            print("%d is Febrary and please input right day( <=28)" %(start_month))
            exit(1)
        rest_day=28 - start_day + 1 #2月当月剩余天数（含请假当天）
    else:
        if start_day > 31:
            print("%d is big month and please input right day( <=31)" %(start_month))
            exit(1)
        rest_day=31 -start_day + 1 #大月当月剩余天数（含请假当天）
    if rest_day < 0:
        print("please input right start day")
        exit (1)
    days=0

    for month in range(1,6):
        next_month=start_month+month
        if next_month >= 12: #跨年了
            next_month=next_month % 12
        if next_month in small_month: #30天的小月
            days=days+30
        else:
            if next_month == 2: #28天的2月
                days=days+28
            else:
                days=days+31 #31天的大月
    print(start_month,"month rest days:", rest_day,"and next five months days:",days)
    days_n=total_days - rest_day - days #最后一个月还可以请的天数
    if days_n <= 0: #最后一个月天数小于等于0
        lastest_month=start_month +5
        if lastest_month in small_month  and lastest_month !=1:
            days_n=30+days_n
        else:
            if lastest_month == 2:
                days_n=28+days_n
            else:
                days_n=31+days_n
    else:
        lastest_month=start_month +6
    if lastest_month > 12: #跨年了
        lastest_month=lastest_month%12
        cur_year=cur_year+1
    print("end day:",cur_year,"年",lastest_month,"月",days_n)
    Label(top, text="结束日期").grid(row=1, column=0)
    Entry(top, textvariable=v2).grid(row=1, column=1, padx=10, pady=5)  # 用于储存 输入的内容并进行表格式布局
    v2.set(days_n)
    v2.set(str(cur_year)+"."+str(lastest_month)+"."+str(days_n))

if __name__ == "__main__":
    top=Tk()
    top.title("产假计算器")
    Label(top,text="开始日期(格式:年.月.日)").grid(row=0,column=0)
    Label(top, text="请假天数").grid(row=2, column=0)
    Label(top, text="说明：未考虑闰年，基础产假98天+广东省增加产假80天，如遇难产/剖腹产增加30天,所以休假天数只能是178或者208").grid(row=3,column=1,padx=3)
    v1 = StringVar()  # 用于请假开始日期
    v2 = StringVar()   # 用于请假结束日期
    v3 = StringVar()   # 用于请假天数
    v4 = StringVar()  # 用于设置出错信息
    e1 = Entry(top, textvariable=v1)  # 用于储存 输入的内容
    e1.grid(row=0, column=1, padx=10, pady=5)  # 进行表格式布局
    e3 = Entry(top, textvariable=v3)  # 用于储存 输入的内容
    e3.grid(row=2, column=1, padx=10, pady=5)  # 进行表格式布局
    Button(top, text='计算结束日期', command=main).grid(row=4,column=0)  # 点击按钮执行的命令
    Button(top, text='Quit', command=top.quit).grid(row=4, column=1)
    top.mainloop()
    #main(sys.argv[1])
    #main(5.14)

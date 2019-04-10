#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
(多行注释使用三个英文的双引号)
产假计算器:
    产假计算工具：基础产假98天+广东省增加产假80天，如遇难产/剖腹产增加30天，所以休假天数只能是178或者208
    使用说明：python Maternity_leave.py
    闰年:能被4整除但不能被100整除的年份，比如2004年
"""

import sys
import time
from tkinter import *
import tkinter.messagebox
# import tkinter as tk

def main():
    start_date = e1.get()  # e1.get()是字符串，此处不能强制转换为int类型
    if "." not in start_date:
        tkinter.messagebox.showerror('报错', '输入格式有误，请输入正确格式的开始日期，即年.月.日')
        exit(1)
    total_days = e3.get()
    total_days = int(total_days)
    if total_days != 178 and total_days !=208:
        tkinter.messagebox.showerror('报错', '请输入正确的休假天数')
        exit(1)
    # total_days=98 +80
    # cur_year=time.strftime("%Y",time.localtime(time.time()))
    try:
        cur_year = start_date.split(".")[0]
        cur_year = int(cur_year)
    except:
        if isinstance(cur_year, int):  # 判断是不是int类型
            print("input date format is right")
        else:
            tkinter.messagebox.showerror('报错', '输入格式有误，请输入正确格式的开始日期，即年.月.日')
            exit(1)
    else:
        print("ok")
    big_year_flag = 0  # 平年
    if cur_year % 4 == 0 and cur_year % 100 != 0:
        big_year_flag = 1  # 闰年，2月有29天，比如2004年
    print("start_day:", start_date, "total days:", total_days)
    try:
        start_day = start_date.split(".")[-1]  # 获取请假开始日期，比如5.14，那么开始日期就是14号
        start_day = int(start_day)
    except :
        if isinstance(start_day, int):  # 判断是不是int类型
            print("input date format is right")
        else:
            tkinter.messagebox.showerror('报错', '输入格式有误，请输入正确格式的开始日期，即年.月.日')
            exit(1)
    else:
        print("ok")

    small_month = [4, 6, 9, 11]
    start_month = start_date.split(".")[1]  # 获取请假开始月份，比如5.14，那么开始月份就是5月
    start_month = int(start_month)
    if start_month > 12:
        tkinter.messagebox.showerror('报错', '请输入正确的月份（小于等于12）')
        exit(1)
    if start_month in small_month and small_month != 1:
        if start_day > 30 or start_day < 1:
            tkinter.messagebox.showerror('报错', '该月份是小月，请输入正确的天数（1-30）')
            # print("%d is small month and please input right day( <=30)" %(start_month))
            exit(1)
        rest_day = 30 - start_day + 1  # 小月当月剩余天数（含请假当天）
    elif start_month == 2:
        if big_year_flag == 1:  # 闰年
            if start_day > 29 or start_day < 1:
                tkinter.messagebox.showerror('报错', '请输入2月份正确的天数（1-29）')
                exit(1)
            rest_day = 29 - start_day + 1  # 2月当月剩余天数（含请假当天）
        else:  # 平年
            if start_day > 28 or start_day < 1:
                tkinter.messagebox.showerror('报错', '请输入2月份正确的天数（1-28）')
                exit(1)
            rest_day = 28 - start_day + 1  # 2月当月剩余天数（含请假当天）
    else:
        if start_day > 31 or start_day < 1:
            tkinter.messagebox.showerror('报错', '该月份是大月，请输入正确的天数(1-31）')
            exit(1)
        rest_day = 31 - start_day + 1  # 大月当月剩余天数（含请假当天）
    if rest_day < 0:
        tkinter.messagebox.showerror('报错', '请输入正确的请假开始日期')
        exit(1)
    days = 0

    for month in range(1, 6):
        next_month = start_month+month
        if next_month >= 12:  # 跨年了
            next_month = next_month % 12
        if next_month in small_month:  # 30天的小月
            days = days + 30
        else:
            if next_month == 2:  # 2月
                if big_year_flag == 1:  # 闰年
                    days = days + 29
                else:
                    days = days + 28
            else:
                days = days + 31  # 31天的大月
    print(start_month, "month rest days:", rest_day, "and next five months days:", days)
    days_n = total_days - rest_day - days  # 最后一个月还可以请的天数
    if days_n <= 0:  # 最后一个月天数小于等于0
        lastest_month = start_month + 5
        if lastest_month in small_month and lastest_month != 1:
            days_n = 30 + days_n
        else:
            if lastest_month == 2:
                if big_year_flag == 1:
                    days_n = 29 + days_n   # 闰年
                else:
                    days_n = 28 + days_n
            else:
                days_n = 31 + days_n
    else:
        lastest_month = start_month + 6
    if lastest_month > 12:  # 跨年了
        lastest_month = lastest_month % 12
        cur_year = cur_year + 1
    print("end day:", cur_year, "年", lastest_month, "月", days_n)
    Label(top, text="结束日期").grid(row=1, column=0)
    Entry(top, textvariable=v2).grid(row=1, column=1, padx=10, pady=5)  # 用于储存 输入的内容并进行表格式布局
    v2.set(days_n)
    v2.set(str(cur_year)+"."+str(lastest_month)+"."+str(days_n))

if __name__ == "__main__" :
    top = Tk()
    top.title("产假计算器")
    Label(top, text="开始日期(格式:年.月.日)").grid(row=0, column=0)
    Label(top, text="休假天数").grid(row=2, column=0)
    Label(top, text="说明：基础产假98天+广东省增加产假80天，如遇难产/剖腹产增加30天,所以休假天数只能是178或者208").grid(row=3, column=1)
    v1 = StringVar()  # 用于请假开始日期
    v2 = StringVar()   # 用于请假结束日期
    v3 = StringVar()   # 用于请假天数
    e1 = Entry(top, textvariable=v1)  # 用于储存 输入的内容
    e1.grid(row=0, column=1, padx=10, pady=5)  # 进行表格式布局
    e3 = Entry(top, textvariable=v3)  # 用于储存 输入的内容
    e3.grid(row=2, column=1, padx=10, pady=5)  # 进行表格式布局
    Button(top, text='计算结束日期', command=main).grid(row=4, column=0)  # 点击按钮执行的命令
    Button(top, text='关闭', command=top.quit).grid(row=4, column=1)
    top.mainloop()
    # main(sys.argv[1])
    # main(5.14)

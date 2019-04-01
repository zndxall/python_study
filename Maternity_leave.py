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

def main(start_date):
    total_days=98 +80
    cur_year=time.strftime("%Y",time.localtime(time.time()))
    print("start_day:",cur_year,start_date,"total days:",total_days)
    start_day=str(start_date).split(".")[-1] #获取请假开始日期，比如5.14，那么开始日期就是14号
    start_day=int(start_day)
    small_month=[4,6,9,11]
    start_month=str(start_date).split(".")[0] #获取请假开始月份，比如5.14，那么开始月份就是5月
    start_month=int(start_month)
    if start_month in small_month and small_month != 1:
        rest_day=30 - start_day
    elif start_month==2:
        rest_day=28 - start_day
    else:
            rest_day=31 -start_day
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

if __name__ == "__main__":
    main(sys.argv[1])
    #main(5.14)
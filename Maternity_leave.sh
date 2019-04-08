#!/usr/bin/sh
#产假计算工具（未考虑闰年），比如从五月某天开始，脚本后跟请假日期，如：sh Maternity_leave.sh 5.14
#基础产假98天+广东省增加产假80天，如遇难产/剖腹产增加30天
total_days=`expr 98 + 80`
#total_days=`expr 98 + 80 + 30`
cur_year=`date "+%Y"`
echo start day: $cur_year.$1 and total days:$total_days
start_month=`echo $1 |awk -F "." '{print $1}'`
[ $start_month -gt 12 ] && echo "please input right month (<=12)" && exit 1
start_day=`echo $1 |awk -F "." '{print $2}'`
small_month="4 6 9 11"
fit_cur_month=`echo $small_month |grep $start_month`
if [ "x$fit_cur_month" != "x" -a "$start_month" != "1" ];then
	[ $start_day -gt 30 ] && echo "$start_month is small month and please input right day( <=30)" && exit 1
        rest_day=`expr 30 - $start_day + 1 ` #小月当月剩余的天数(含请假当天)
else
    if [ "$start_month" == "2" ];then
	[ $start_day -gt 28 ] && echo "$start_month is February and please input right day( <=28)" && exit 1
        rest_day=`expr 28 - $start_day + 1` #2月当月剩余的天数(含请假当天)
    else
	[ $start_day -gt 31 ] && echo "$start_month is big month and please input right day( <=31)" && exit 1
	rest_day=`expr 31 - $start_day + 1  ` #大月当月剩余的天数(含请假当天)
    fi
fi
[ $rest_day -lt 0 ] && echo please input right start day && exit 1
days=0
for ((months=1;months<=5;months++))
do
	next_month=`expr $start_month + $months`
	[ $next_month -gt 12 ] && next_month=$(($next_month % 12 )) #跨年了
	fit_small_month=`echo $small_month | grep $next_month`
	if [ "x$fit_small_month" != "x" ];then #30天的小月
	    days=`expr $days + 30`
	else
	    if [ "$next_month" == "2" ]; then
	        days=`expr $days + 28` #2月按照28天
	    else
	        days=`expr $days + 31` #31天的大月
            fi
	fi
done
echo $start_month month rest days: $rest_day and next five months days:$days
days_n=`expr $total_days - $rest_day - $days` #最后一个月还可以请的天数
if [ $days_n -le 0 ];then #最后一个天数小于等于0
    echo "$days_n < = 0 "
    lastest_month=`expr $start_month + 5` #最后一个月的月份
    fit_last_month=`echo $small_month |grep $lastest_month`
    #因为days_n是负数了，所以要使用加
     if [ "x$fit_last_month" != "x" -a "$lastest_month" != "1" ];then
        days_n=`expr 30 + $days_n `
    else
        if [ "$lastest_month" == "2" ];then
            days_n=`expr 28 + $days_n `
        else
            days_n=`expr 31 + $days_n `
        fi
    fi
else
    lastest_month=`expr $start_month + 6` #最后一个月的月份
fi
[ $lastest_month -gt 12 ] && lastest_month=$(($lastest_month % 12 )) && cur_year=`expr $cur_year + 1` #跨年了
echo end day: $cur_year.$lastest_month.$days_n


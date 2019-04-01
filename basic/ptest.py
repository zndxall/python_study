#!/usr/bin/env python
#coding=utf-8
import os,subprocess #输入输出
import sys #参数处理
from datetime import datetime
import time
import shutil
import putil
print("jenkins var as follow:")
#print os.getenv("BUILD_NUMBER")
print("job_number=",os.getenv("BUILD_NUMBER"))
print("job_user_id=",os.getenv("BUILD_USER_ID"))
print("job_user=",os.getenv("BUILD_USER"))
print("job_name=",os.getenv("JOB_NAME"))
trigger_user=os.getenv("BUILD_USER_ID")
for num in range(1,len(sys.argv)):
    print("%d is %s" %(num,sys.argv[num]))
 #获取参数个数，并赋值
print("var num=%d" %(num))
phoenix_channel=sys.argv[1]
phoenix_type=sys.argv[2]
ph_branch_tmp=sys.argv[3]
phoenix_repo=sys.argv[4]
apk_path=""
if num == 5 :
    apk_path=sys.argv[5]
    print("apk_path=",apk_path)
print("config: %s %s %s %s %s " %(trigger_user,phoenix_channel,phoenix_type,ph_branch_tmp,phoenix_repo))

cur_path=os.path.abspath(".") #获取当前路径
more_flag="0"
if ',' in phoenix_channel:
    more_flag="1"
if phoenix_repo == "rec_app" or phoenix_repo == "send_app" :
    if phoenix_channel == "app_stores":
        if phoenix_repo == "rec_app" :
            shutil.copy('/usr/local/scripts/build_scripts/all_channels',cur_path)
        else:
            shutil.copy('/usr/local/scripts/build_scripts/mobile_assistant',cur_path)

        #删除文件中的空行
        os.popen("sed -i /^\s*$/d " + all_channels)
        channels_file="all_channels"
    else:#将渠道写入文件中
        with open('app_channels','w') as fchannels:
            fchannels.write(phoenix_channel)
        if more_flag != "1":
            print("just only input one channel =",phoenix_channel)
        else:
            print("user input one more channel =",phoenix_channel)
            with open('app_channels','r') as fapp:
                with open('app_channels.bak','w') as fapp_bak :
                    for app_line in fapp:
                        fapp_bak.write(app_line.replace(',','\n'))
            os.remove("app_channels")
            os.rename("app_channels.bak","app_channels")
        print("app channels as follow:")
        print(open('app_channels','r').read())
        channels_file="app_channels"

    if apk_path != "" :
        apk_path=apk_path.replace('\\','/').replace('/ftp','') #将路径中的\\替换成/，并删除其中的/ftp
        print(os.popen("curl -u aolingli:ALL1234! ftp:%s/ > ftp_info" %(apk_path)).read()) #执行获取路径信息的shell命令
        with open('ftp_info','r') as fftp_info:
            for fline in fftp_info.readlines():
                if '.apk' in fline:
                    dapk_name=fline.split(' ')[-1].replace('\n','') #获取下载的apk的名字，路径信息包含.apk的那条信息的最后一个字段
                    print("dapk_name=",dapk_name)
                    break
        os.makedirs("download_target") #创建文件加
        print(os.popen("curl -u aolingli:ALL1234! -o download_target/%s ftp:%s/%s" %(dapk_name,apk_path,dapk_name)).read()) #下载apk
        with open(channels_file,'r') as p_file:
            for my_ch in p_file:
                my_ch=my_ch.replace('\n','')
                dapk_name=dapk_name.replace('\n','')
                print("++++++++++++++ %s packaging ++++++++++" %(my_ch))
                os.makedirs("target")
                shutil.copy(os.path.join(cur_path,"download_target/",dapk_name) ,os.path.join(cur_path,"target")) #将download_target下的apk复制到target下
                if phoenix_repo == "rec_app" :
                    print("rec_app")
                    putil.phoenix_app_special_channels(dapk_name,my_ch) #对特殊渠道做处理，比如换app名字，图片等
                    putil.replace_channel_conf(dapk_name,my_ch,"rec_app_info.conf") #添加渠道信息，包含appid,secret,渠道名
                else:
                    print("send_app")
                    putil.replace_channel_conf(dapk_name,my_ch,"send_app_info.conf")
                print("target file:",os.popen("ls target").read()) #显示target下的文件
                if phoenix_repo == "rec_app" :
                    u_module="phoenix_app"
                else:
                    u_module="phoenix_send_app"
                u_app_command="curl -u aolingli:ALL1234! -T target/%s ftp://192.168.8.251/output/%s/public_channels/" %(dapk_name.replace('happytest',my_ch),u_module)
                print(os.popen(u_app_command).read()) #上传文件到ftp下
                print("ftp_path=\\\\192.168.8.251\\ftp\\output\\%s\\public_channels" %(u_module))
        exit (0)

if os.getenv("BUILD_USER_ID") == "":
    trigger_user=os.getenv("BUILD_USER") #换取环境变量的值
if os.getenv("BUILD_USER") == "":
    trigger_user="Timer" 
print("user %s trigge this build" %(trigger_user))
os.popen("chmod 777 gradlew")
if phoenix_repo=="rec_app" or phoenix_repo=="send_app":
    ftag= open('build_tags','r')
    for line in ftag.readlines():
         print(line[0:7])
         if line[0:7] == "apk_tag":
             apk_tag=line[8:] #获取tag
             break
    ftag.close()
    if apk_tag.strip() != "":
        print("apk tag is  not null :",apk_tag )
        os.popen("git checkout " + apk_tag) #切换到对应tag
        ph_branch_tmp=apk_tag
    if apk_tag.strip() == "":
        print("apk tag is null")
        os.popen("git checkout " + ph_branch_tmp) #切换到对应分支
        os.popen("git pull ")

commit_id=os.popen("git rev-parse --short HEAD ").read().replace('\n','') #获取commitid
ph_branch=ph_branch_tmp.replace('.','')
time_now=datetime.now().strftime("%Y%m%d%H%M") #按照指定格式获取当前时间
now_time=time_now+'_'+ph_branch+'_'+commit_id+'_'+trigger_user+'_'+phoenix_channel+'_'+phoenix_type #上传文件夹名字的拼接
old_channel=phoenix_channel

if phoenix_repo == "rec_app" :
    if not os.path.isfile('usr/local/scripts/build_scripts/local.properties'): #判断文件是否存在
        print ("file is not exist")
    else:
        shutil.copy('usr/local/scripts/build_scripts/local.properties',cur_path)
    ph_ftp_dir="phoenix_app"
    phoenix_channel=""

if phoenix_repo == "send_app" :
    ph_ftp_dir="phoenix_send_app"
    phoenix_channel=""

build_command="sh build.sh %s %s" %(phoenix_channel,phoenix_type)
print(build_command)
print(os.popen(build_command).read()) #执行打包脚本
target_path=os.path.join(cur_path,'target')
target_list=list(x for x in os.listdir(target_path)) #显示target路径下的文件
print(target_list)  
with open(os.path.join(cur_path,'sdkinfo'),'w') as fcurl:
    fcurl.write("sdk version:")









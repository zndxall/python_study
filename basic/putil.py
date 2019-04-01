#!/usr/bin/env python
#coding=utf-8
import os
import shutil
import linecache
import zipfile

def copyfile(src,dst):
    print("move %s --> %s" %(src,dst))
    shutil.copy(src,dst) #复制文件
    print("new dst size:", os.path.getsize(dst)) #计算文件大小

def Change_AppName(apk_name,channel,changestr): #修改中文英文繁体的app名字
    print("channel:%s,changestr:%s" %(channel,changestr))
    for value_path in [ 'values','values-zh-rCN','values-zh-rHK','values-zh-rTW' ]:
        strf=open(os.path.join(apk_name,"res/",value_path,"strings.xml"),'r') 
        strf_new=open(os.path.join(apk_name,"res/",value_path,"strings.xml.bak"),'w')
        for str_line in strf.readlines():
            if "app_name" in str_line:
                old_str=str_line.strip('\n')
                if channel == "damai_inner" or channel == "damai_oversea" :
                    if value_path == "values-zh-rCN":
                        new_string="app_name\">大麦"
                    if value_path == "values-zh-rHK" or value_path == "values-zh-rTW":
                        new_string="app_name\">大麥"
                    if value_path == "values":
                        new_string="app_name\">%s"%(changestr)
                else:
                    new_string="app_name\">%s"%(changestr)
                new_str=old_str.replace("app_name\">",new_string)
                strf_new.write(new_str)
            else:
                strf_new.write(str_line)
        strf.close()
        strf_new.close()
        os.remove(os.path.join(apk_name,"res/",value_path,"strings.xml")) #删除老的string.xml 
        os.rename(os.path.join(apk_name,"res/",value_path,"strings.xml.bak"),os.path.join(apk_name,"res/",value_path,"strings.xml")) #重命令文件

    print("change result as follow:")#检查app名称是否修改成功
    for value_path in [ 'values','values-zh-rCN','values-zh-rHK','values-zh-rTW' ]:
        with open(os.path.join(apk_name,"res/",value_path,"strings.xml"),'r') as strf_n:
            for str_line_n in strf_n.readlines():
                if "app_name" in str_line_n:
                    print(str_line_n)
                    break

def phoenix_app_special_channels (apk_name,channel):
    print("var =%s,%s" %(apk_name,channel))
    cur_path=os.path.abspath(".")
    tool_path="/usr/local/scripts/build_scripts/sign_apk_tool"
    if channel != "alibaba" and channel != "damai_inner" and channel != "damai_oversea" and channel != "konka" and channel != "skyworthbox" :
        print("not alibaba,damai_inner,damai_oversea,konka,skyworthbox channel,so do nothing and return")
        return
    os.makedirs("sign_apk_tool")
    shutil.copy(os.path.join("target",apk_name),"sign_apk_tool")
    os.chdir("sign_apk_tool")
    old_apk_name=apk_name.split(".apk")[0]
    print("old_apk_name: ", old_apk_name)
    
    print(" ================================apktool decompile===========================")
    print(os.popen("java -jar %s d %s" %(os.path.join(tool_path,"apktool.jar"),apk_name)).read())
    print("delete %s ..." %(apk_name))
    os.remove(apk_name)

    #alibaba和康佳的apk名字和启动页上要加上CIBN字样
    if channel == "alibaba" or channel == "konka" :
        print("%s channel need to change app name and add CIBN" %(channel))
        Change_AppName(old_apk_name,channel,"CIBN")
        copyfile(os.path.join(tool_path,"ali/","ali_lunch.png") ,os.path.join(old_apk_name,"res/","mipmap-xhdpi-v4/","lunch_bg.png"))

    #大麦(1)修改apk名字,(2)替换bg_main_video.png(3)替换优化页(4)替换icon(5)替换启动页(6)替换devicename.txt文件(7)删除homepage
    if channel == "damai_inner" or channel == "damai_oversea" :
        print("%s channel need to change app name and add damai" %(channel))
        Change_AppName(old_apk_name,channel,"Damai")
        copyfile(os.path.join(tool_path,"damai/","bg_main_video.png"),os.path.join(old_apk_name,"res/","mipmap-xhdpi-v4/","bg_main_video.png"))
        copyfile(os.path.join(tool_path,"damai/","cast_optimize.png"),os.path.join(old_apk_name,"res/","drawable/","cast_optimize.png"))
        copyfile(os.path.join(tool_path,"damai","damai_lunch_pg.png"),os.path.join(old_apk_name,"res/","mipmap-xhdpi-v4/","lunch_bg.png"))
        copyfile(os.path.join(tool_path,"damai/","devicenames.txt"),os.path.join(old_apk_name,"res/","raw/","devicenames.txt"))
        fr=open(os.path.join(old_apk_name,"res/","raw/","devicenames.txt"),'r')
        print(fr.read())
        fr.close()
            
        
    print("==============================delete META-INF ===================")
    shutil.rmtree(os.path.join(old_apk_name,"original/","META-INF"))
    print(" ================================apktool compile============================")
    print(os.popen("java -jar %s b %s" %(os.path.join(tool_path,"apktool.jar"),old_apk_name)).read())
    shutil.move(os.path.join(old_apk_name,"dist/",apk_name), os.path.abspath(".") )

    print("===================================sign====================================")
    sign_command="jarsigner -verbose -digestalg SHA1 -sigalg SHA1withRSA -keystore %s -signedjar %s  %s mirrorcast_aw -storepass mirrorcastisgood" %(os.path.join(tool_path,"mirrorcast_aw.key"),apk_name,apk_name)
    print(os.popen(sign_command).read())

    print("==================================checking sign=============================")
    print(os.popen("jarsigner -certs -verify %s" %(apk_name)).read())
    os.chdir(cur_path)
    shutil.move(os.path.join("sign_apk_tool",apk_name),os.path.join("target",apk_name))
    print("cur_path:",os.path.abspath("."))

def addFileIntoZipfile(srcDir,fp):
    for subpath in os.listdir(srcDir):
        subpath=os.path.join(srcDir,subpath)
        if os.path.isfile(subpath):
            fp.write(subpath)   #写入文件
        elif os.path.isdir(subpath):
            fp.write(subpath)   #写入文件
            addFileIntoZipfile(subpath,fp)  #递归调用
          
def zipCompress(srcDir,desZipfile):
    with zipfile.ZipFile(desZipfile,mode='a') as fp: #以追加模式打开或创建zip文件
        addFileIntoZipfile(srcDir,fp)

def replace_channel_conf (apk_name,channel,conf_file):
    print("var:%s %s %s" %(apk_name,channel,conf_file))
    old_apk_name=apk_name 
    apk_name=apk_name.replace('happytest',channel)
    os.rename(os.path.join("target",old_apk_name),os.path.join("target",apk_name))
    cur_path=os.path.abspath(".")
    conf_file_path="/usr/local/scripts/build_scripts/%s" %(conf_file)
    shutil.copy(conf_file_path,os.path.abspath("."))
    conf_file=os.path.join(os.path.abspath("."),conf_file)
    print(conf_file)
    conf_f=open(conf_file,'r')
    line_num=0
    ch_have_flag=0
    for appid_flag in conf_f.readlines():
        if channel in appid_flag :
            ch_have_flag=1
            print("fit:",appid_flag.strip('\n'),line_num)
            break
        line_num+=int(1)
    conf_f.close()
    print("new_num=",line_num)
    if ch_have_flag == 0 :
        print("not find %s in %s ,fail." %(channel,conf_file))
        exit (1)
    appid_tmp=linecache.getlines(conf_file)[line_num + int(1)].strip('\n')
    appid=appid_tmp[7:]
    secret_tmp=linecache.getlines(conf_file)[line_num + int(2)].strip('\n')
    secret=secret_tmp[7:]
    print("channel info:",channel,appid,secret)
    os.makedirs("META-INF")
    for app_conf in [ appid,secret,channel ]:
        if app_conf == appid:
            app_f="appid_%s"%(app_conf)
        if app_conf == secret:
            app_f="secret_%s"%(app_conf)
        if app_conf == channel:
            app_f="channel_%s"%(app_conf)
        fapp=open(os.path.join("META-INF",app_f),'w')
        fapp.close()
    zipCompress('META-INF',os.path.join("target",apk_name))
    os.makedirs("apk_output")
    shutil.copy(os.path.join("target",apk_name),"apk_output")
    os.chdir("apk_output")
    print("unzip %s to check" %(apk_name))
    azip = zipfile.ZipFile(apk_name)
    azip.extractall()
    azip.close()
    for app_f_new in os.listdir(os.path.join(cur_path,"META-INF")):
        if os.path.exists(os.path.join("META-INF",app_f_new)):
            print("add %s success" %(app_f_new))
        else:
            print("add %s failed and exit" %(app_f_new))
    os.chdir(cur_path)
    print("cur_path:",os.path.abspath("."))

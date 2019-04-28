#!/usr/bin/env python
# coding=utf-8
import os
def get_line(file_name):
    count = 0
    with open(file_name,'rb') as rfile:
        for file_line in rfile.readlines():
            if file_line != '' and file_line != '\n':  # 排除文件中的换行空行
                count += 1
    # print("%s=%d" %(file_name,count))
    return count

def all_dir(dir_path) :
    files = os.listdir(dir_path)
    for fs_d in files:
        if fs_d == ".git":
            continue
        else:
            fs_dpath = os.path.join(dir_path,fs_d)
            if os.path.isdir(fs_dpath):
                all_dir(fs_dpath)
            else:
                if os.path.splitext(fs_dpath)[1] == '.sh' or os.path.splitext(fs_dpath)[1] == '.py':  # 只统计shell脚本和python脚本的行数
                    line_counts = get_line(fs_dpath)
                    print("%s=%d" % (fs_dpath, line_counts))
                else:
                    continue

if __name__ == "__main__":
    path_dir = os.path.abspath(".")  # 获取当前目录
    all_dir(path_dir)
    #for i in os.walk(path_dir):
    #   print(i)

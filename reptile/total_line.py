#！/usr/bin/env python
#coding=utf-8
import os
def get_line(file_name):
    count=0  
    with open(file_name,'r',encoding='UTF-8') as rfile:
        for file_line in rfile.readlines():
            if file_line != '' and file_line != '\n' :
                count +=1
    print("%s count lines=%d" %(file_name,count))
    return count

if __name__ == "__main__":
    total_line=0
    for file_n in os.listdir(os.path.abspath(".")):
        file_path=os.path.join(os.path.abspath("."),file_n)
        if os.path.isfile(file_path):
            total_line=total_line+get_line(file_n)
    print("total_line=",total_line)

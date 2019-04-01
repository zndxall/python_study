#！/usr/bin/env python
#coding=utf-8
import urllib.request
import re
def get_html(url):
	page=urllib.request.urlopen(url) 
	htmlcode=page.read()
	#print(htmlcode)
	with open('pagecode.html','wb+') as pagefile:
		pagefile.write(htmlcode)
	return htmlcode

def get_image(html_code):
	#reg=r'src="(.+?\.(jpg|JPG|png|PNG|gif))" width' #图片的正则表达式
	reg=r'src="(.+?\.jpg)" width' #图片的正则表达式
	#reg=r'src="(.+?\.png)" width' #图片的正则表达式
	reg_img=re.compile(reg) #编译一下，运行更快
	html_code=html_code.decode('utf-8') #python3，不加这一行会报错
	imglist=reg_img.findall(html_code) #查找网页中的满足正则表达式的所有图片
	print(type(imglist))
	x=0
	for img in imglist:
		print("download img:",img)
		urllib.request.urlretrieve(img,'%s.jpg' %x) #下载图片
		x +=1

if __name__ == "__main__": #程序入口
	#url_name=input('请输入url:')
	#if url_name:
	#	pass
	#else:
	#	url_name='http://tieba.baidu.com/p/1753935195'
	print("=======网页图抓取=========")
	url_name='http://tieba.baidu.com/p/1753935195'
	#url_name='https://www.cnblogs.com/zndxall/p/9586088.html'
	print("url_name=",url_name)
	html_var=get_html(url_name)
	get_image(html_var)




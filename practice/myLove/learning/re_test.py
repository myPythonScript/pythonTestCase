#coding=utf-8
import requests
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
res = requests.get('https://movie.douban.com/chart',headers = headers)
results = re.findall(r'<img src="(.*).png".*',res.text)
for i in results:
	print(i)
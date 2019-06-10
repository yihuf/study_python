#coding:utf-8
import urllib.request

url = 'http://tieba.baidu.com/p/5985949894'

header = {
'User-Agent':	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
}

req = urllib.request.Request(url, headers=header)
page = urllib.request.urlopen(req)
htmlcode = page.read()#读取页面源码

htmlfile = open('test.html', 'w+', encoding='utf-8')

print(type(htmlcode))
htmlfile.write(str(htmlcode, 'utf-8'))
htmlfile.close()


#coding:utf-8
import urllib2
import re


url = 'http://www.my285.com/zt/dygw/index.htm'
page = urllib2.urlopen(url)
htmlcode = page.read()#读取页面源码

reg = r'<a href="(.+?)">(.+?)</a></td>'

results = re.findall(reg, htmlcode)

titles = []
for result in results:
    title = result[1].decode('gbk')
    tmp_title = [result[0].replace('/index.htm', ''), title]
    titles.append(tmp_title)

page_reg = r'<a href="(.+?)">.*</a></td>'
for num, title in enumerate(titles):
    print('第%d本，总共%d本' % ((num +1), len(titles)))
    print(title[1])
    txt_file = open(title[1]+'.txt', 'w+')
    tmp_url = 'http://www.my285.com/zt/dygw/%s/index.htm' % title[0]
    tmp_page = urllib2.urlopen(tmp_url)
    tmp_htmlcode = tmp_page.read()#读取页面源码
    page_results = re.findall(page_reg, tmp_htmlcode)
    for i, page_result in enumerate(page_results):
        page_url = 'http://www.my285.com/zt/dygw/%s/%s' % (title[0], page_result)
        page_txt = urllib2.urlopen(page_url)
        page_txt_reg = r'^(.*?)<br>'
        for line in page_txt.readlines():
            line_text = re.findall(page_txt_reg, line)
            if len(line_text) != 0:
                txt_file.write(line_text[0]+'\n')

    txt_file.close()


print('all write over')






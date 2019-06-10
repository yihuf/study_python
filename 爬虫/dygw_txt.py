#!/bin/python
#coding=utf-8

import urllib2
import re
import sys
import time
import os
import multiprocessing

from log import my_logger

def worker(title):
    my_logger.info(title[1])
    txt_file = open('result/'+title[1]+'.txt', 'w+')
    tmp_url = 'http://www.my285.com/zt/dygw/%s/index.htm' % title[0]
    tmp_page = urllib2.urlopen(tmp_url)
    tmp_htmlcode = tmp_page.read()
    page_results = re.findall(page_reg, tmp_htmlcode)
    for i, page_result in enumerate(page_results):
        page_url = 'http://www.my285.com/zt/dygw/%s/%s' % (title[0], page_result)
        page_txt = urllib2.urlopen(page_url)
        page_txt_reg = r'^(.*?)<br>'
        for line in page_txt.readlines():
            line_text = re.findall(page_txt_reg, line)
            if len(line_text) != 0:
                #print(line_text[0].decode("gbk"))
                txt_file.write(line_text[0].decode("gbk") + "\n")

    txt_file.close()


reload(sys)
sys.setdefaultencoding("utf-8")

if not os.path.exists('result'):
   os.mkdir('result', 755)
   
start_time = time.ctime()
url = 'http://www.my285.com/zt/dygw/index.htm'
page = urllib2.urlopen(url)
htmlcode = page.read()

reg = r'<a href="(.+?)">(.+?)</a></td>'

results = re.findall(reg, htmlcode)

titles = []
for result in results:
    title = result[1].decode('gbk')
    tmp_title = [result[0].replace('/index.htm', ''), title]
    titles.append(tmp_title)

page_reg = r'<a href="(.+?)">.*</a></td>'
for num, title in enumerate(titles):
    my_logger.info('第%d本，总共%d本' % ((num +1), len(titles)))
    p = multiprocessing.Process(target=worker, args=(title,))
    p.start()
    p.join()

my_logger.info('all write over')
end_time = time.ctime()

my_logger.info('start time:'+str(start_time))
my_logger.info('end time:'+str(end_time))





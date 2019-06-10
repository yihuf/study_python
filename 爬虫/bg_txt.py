#coding:utf-8
import urllib2
import re
import time
import sys

from log import my_logger

reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://www.8wenku.com/chapter/view?id=2775&chapter_no='

my_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

start_time = time.ctime()

reg = r'^(.*?)<br />'

my_file = open(u'冰菓.txt', 'w+')

for i in range(1, 55):
    page_url = url + str(i)
    req = urllib2.Request(page_url, headers=my_headers)
    page = urllib2.urlopen(req)
    for line in page.readlines():
        line_texts = re.findall(reg, line)
        if len(line_texts) != 0:
            line_text = line_texts[0]
            my_logger.debug(line_text)
            my_file.write(line_text + '\n')


my_file.close()
my_logger.info('all read over')
end_time = time.ctime()

my_logger.info('start time:'+str(start_time))
my_logger.info('end time:'+str(end_time))

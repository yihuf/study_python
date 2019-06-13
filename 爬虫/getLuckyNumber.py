#coding:utf-8

import urllib2
import urllib
import json


def get_lottery_type():
    url = 'http://apis.juhe.cn/lottery/types'
    param = {
        'key': 'abcc8a2310a36c42c29d3a3791ac3ca5'
    }
    data = urllib.urlencode(param)
    response = urllib2.urlopen(url, data).read()
    print(response)
    resp = json.loads(response)
    lottery_id = ''
    for result in resp['result']:
        print(result['lottery_name'])
        if result['lottery_name'] == u'双色球':
            lottery_id = result['lottery_id']
            print(lottery_id)
            break

    return lottery_id


def get_lottery_res(page, lottery_id):
    url = 'http://apis.juhe.cn/lottery/history'
    param = {
        'key': 'abcc8a2310a36c42c29d3a3791ac3ca5',
        'lottery_id': lottery_id,
        'page_size': '50',
        'page': page
    }
    data = urllib.urlencode(param)
    response = urllib2.urlopen(url, data).read()
    print(response)
    resp = json.loads(response)
    results = []
    for result in resp['result']['lotteryResList']:
        results.append(result['lottery_res'])

    return results


def get_lucky_number(history_list):
    red_res = []
    blue_res = []
    for history in history_list:
        res = history.split(',')
        red_res += res[:6]
        blue_res += res[6:7]
    red_res_count = {}
    blue_res_count = {}
    for key in red_res:
        if not red_res_count.has_key(key):
            red_res_count[key] = 1
        else:
            red_res_count[key] += 1

    for key in blue_res:
        if not blue_res_count.has_key(key):
            blue_res_count[key] = 1
        else:
            blue_res_count[key] += 1

    sorted_red_res_count = sorted(red_res_count.items(), key=lambda red_res_count: red_res_count[1])
    sorted_blue_res_count = sorted(blue_res_count.items(), key=lambda blue_res_count: blue_res_count[1])

    print(sorted([item[0] for item in sorted_red_res_count[:6]]))
    print([item[0] for item in sorted_blue_res_count[:1]])


all_result = []
lottery_type = get_lottery_type()
for i in range(1, 11):
    all_result += get_lottery_res(str(i), lottery_type)

print(all_result)

# 获取最近100次结果中出现次数最少的号码
get_lucky_number(all_result[:100])
# 获取最近200次结果中出现次数最少的号码
get_lucky_number(all_result[:200])
# 获取最近300次结果中出现次数最少的号码
get_lucky_number(all_result[:300])
# 获取最近400次结果中出现次数最少的号码
get_lucky_number(all_result[:400])
# 获取最近500次结果中出现次数最少的号码
get_lucky_number(all_result[:500])

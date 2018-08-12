#coding:utf-8
import urllib.request
import re
import base64
import rsa
import binascii
import http.cookiejar
import time
import json

# 预配置参数，此处由使用者自己填写
my_username = '18827070643'
my_password = 'huyi3313825833'
dst_id = '1005052805895234'  #进入目标主页，查看目标粉丝，url里面的id即为dst_id

logfile = open('log.html', 'w', encoding='utf-8')

# 由dst_id获取
dst_domain = dst_id[:6] #domain
dst_uid = dst_id[6:]  #用户id

# 保存cookie
cj = http.cookiejar.LWPCookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)

prelogin_url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&' \
               'su=%s&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.15)&_=1400822309846'%my_username
page = urllib.request.urlopen(prelogin_url)
htmlcode = page.read()#读取页面源码

print(htmlcode)#在控制台输出

# 获取登录所需要的参数
servertime = re.findall('"servertime":(.*?),', str(htmlcode))[0]
pubkey = re.findall('"pubkey":(.*?),', str(htmlcode))[0].strip('"')
rsakv = re.findall('"rsakv":(.*?),', str(htmlcode))[0].strip('"')
nonce = re.findall('"nonce":(.*?),', str(htmlcode))[0].strip('"')

su = base64.b64encode(bytes(urllib.request.quote(my_username), encoding='utf-8'))

rsaPublickey = int(pubkey, 16)
key = rsa.PublicKey(rsaPublickey, 65537)
message = bytes(servertime + '\t' + nonce + '\n' + my_password, encoding='utf-8')
sp = binascii.b2a_hex(rsa.encrypt(message, key))

param = {'entry': 'weibo', 'gateway': 1, 'from': '', 'savestate': 7, 'useticket': 1,
    'pagerefer': 'http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D',
    'vsnf': 1, 'su': su, 'service': 'miniblog', 'servertime': servertime, 'nonce': nonce,
    'pwencode': 'rsa2', 'rsakv': rsakv, 'sp': sp, 'sr': '1680*1050', 'encoding': 'UTF-8', 'prelt': 961,
    'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack'}

headers = {'User-Agent' : 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'}

url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
data = urllib.parse.urlencode(param).encode('utf-8')
myrequest = urllib.request.Request(url=url, data=data, headers=headers)
loginpage = urllib.request.urlopen(myrequest)

loginhtmlcode = loginpage.read().decode('gbk')
print(str(loginhtmlcode))
# 获取跳转的网址
urll = re.findall("location.replace\(\'(.*?)\'\);", str(loginhtmlcode))
if len(urll) == 0:
    urll = re.findall("location.replace\(\"(.*?)\"\);", str(loginhtmlcode))
print(urll)

# 打开跳转的网址
finalpage = urllib.request.urlopen(urll[0])
finalpagecode = finalpage.read()
print('finalpagecode', finalpagecode)
time.sleep(1)

# 到这里为止登录成功

# 开始实现爬取功能
# STEP 1 获取对方关注的目标

fans_url = 'https://weibo.com/p/%s/follow?page=' % dst_id

# 获取目标数目
response = urllib.request.urlopen(fans_url + '1').read()
content = response.decode("utf-8")

reg1 = '>她的关注 (\d*?)<'
reg2 = '>他的关注 (\d*?)<'
result = re.findall(reg1, content)
if len(result) == 0:
    result = re.findall(reg2, content)
follows_num = int(result[0])
print('follows_num', follows_num)

# 保存目标列表(uid, nickname, sex), 如果不是互fo用户，微博不会显示全部目标，并且微博会过滤部分广告目标，因此实际目标数目不等于follows_num
followers = []
reg = 'uid=(\d+?)&fnick=(\S+?)&sex=(\w+?)'
cur_follows_num = 0
i = 1
while True:
    response = urllib.request.urlopen(fans_url + str(i)).read()
    content = response.decode("utf-8")
    result = re.findall(reg, content)
    cur_follows_num = len(result)
    if cur_follows_num == 0:
        break
    followers += result
    i += 1
    print('result', result)


print('followers', len(followers), followers)

# 进入目标微博
userurl = "https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=%s&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&" % dst_domain
final_result = []
for follower in followers:
    # 查询页码
    userpagenumurl = userurl + "page=1&pagebar=1&id=" + dst_domain + follower[0] + "&pre_page=1"
    try:
        pagenumresponse = urllib.request.urlopen(userpagenumurl)
    except:
        continue
    pagenumtext = pagenumresponse.read()
    content = json.loads(pagenumtext.decode("ascii"))['data']
    pagenumreg = re.compile('countPage=(.+?)"')
    pagenum = pagenumreg.findall(content)[0]
    print(follower[1], 'pagenum', pagenum)
    # 获取全部微博内容的mid值
    pageurls = []
    for i in range(1, int(pagenum)+1):
        pageurls.append(userurl+"page="+str(i)+"&pagebar=0&id="+dst_domain+follower[0])
        for j in range(0, 2):
            pageurls.append(userurl+"page="+str(i)+"&pagebar="+str(j)+"&id="+dst_domain+follower[0]+"&pre_page="+str(i))
    mids = []
    for i, pageurl in enumerate(pageurls):
        try:
            mypage = urllib.request.urlopen(pageurl)
        except:
            continue
        myhtmlcode = mypage.read()#读取页面源码
        content = json.loads(myhtmlcode.decode("ascii"))['data']
        reg = 'http://service.account.weibo.com/reportspam\?rid=(\d+?)&from='
        mid = re.findall(reg, str(content))
        mids += mid
        print('pagenum: ', i, 'max', len(pageurls), mid)
    print('mids', mids)

    # 获取用户的全部评论
    reg = u'usercard="id=(\d+?)">(\S+?)</a>：(\S+?) '
    tmp_id = ''
    for mid in mids:
        user_contents = []
        for i in range(1,50):
            url = "https://weibo.com/aj/v6/comment/big?ajwvr=6&id=%s&root_comment_max_id_type=0" \
                  "&root_comment_ext_param=&page=%d&filter=hot&from=singleWeiBo" % (mid, i)
            print(url)
            try:
                mypage = urllib.request.urlopen(url)
            except:
                break
            myhtmlcode = mypage.read()#读取页面源码
            content = json.loads(myhtmlcode.decode("ascii"))['data']
            result = re.findall(reg, str(content))
            if len(result) == 0:
                break
            if tmp_id == result[0][0]:
                break
            tmp_id = result[0][0]
            user_contents += result
        for user_content in user_contents:
            if user_content[0] == dst_uid:
                tmp_result = []
                tmp_result.append(user_content)
                tmp_result.append(mid)
                tmp_result.append(i)
                final_result.append(tmp_result)
                logfile.write(str(tmp_result) + '\n')
                logfile.flush()

for result in final_result:
    print(result)

print('read over')
logfile.close()




















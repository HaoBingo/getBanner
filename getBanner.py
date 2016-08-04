#!/usr/bin/env python
#-*-coding:utf-8-*-
# Data: 2016/8/4
# Created by Bingo
# Blog http://haobingo.com


import requests
import re
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
time_start = time.time()

'''
2016/8/4   V0.1  初版，仅扫描单IP，获取80端口Banner，使用get请求(有些服务器不支持options head)
'''
if len(sys.argv) < 2:
    script = sys.argv[0].split('\\')[-1]
    print "Usage:   %s host" %script
    print "Example: %s 192.168.0.1 " %script
    sys.exit(0)

s = requests.Session()
s.headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

host = sys.argv[1]
url = "http://%s" %host
print url
def getBanner(url):
    try:
        res = s.get(url,timeout=2)
        server =  res.headers["Server"]
        print server
        return server
    except Exception as e:
        print e
        print type(e)
        if e == requests.exceptions.ConnectTimeout:
            print "time out"
            return None
            
server = getBanner(url)
if server != None:
    if "IIS" in server or "Win" in server:
        print "WINDOWS!"
time_stop = time.time()
print "time: %.3f" %(time_stop-time_start)
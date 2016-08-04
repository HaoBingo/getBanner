#!/usr/bin/env python
#-*-coding:utf-8-*-
# Data: 2016/8/4
# Created by Bingo
# Blog http://haobingo.com


import requests
import re
import time
from netaddr import IPNetwork
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


'''
2016/8/4   V0.1  初版，仅扫描单IP，获取80端口Banner，使用get请求(有些服务器不支持options head)
2016/8/4   V0.2  二版，支持网段扫描，获取80端口Banner，使用head请求，扫描C段大概耗时4min
'''

time_start = time.time()
s = requests.Session()
s.headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
serverList = []
windowsList = []

def getBanner(host):
    global serverList
    url = "http://%s" %host
    try:
        res = s.head(url,timeout=1)
        server =  res.headers["Server"]
        #print "Server:  %s" %server
        serverList.append((str(host),server))
        #print serverList
        return server
    except:
        return None
        
def checkBanner(server,host): 
    global windowsList       
    if server != None:
        if "IIS" in server or "Win" in server:
            windowsList.append((str(host),server))

def main():
    if len(sys.argv) < 2:
        script = sys.argv[0].split('\\')[-1]
        print "Usage:   %s host" %script
        print "Example: %s 192.168.0.1 or 192.168.0.1/24 " %script
        sys.exit(0)
    print "This need about 4 mins, Please be patient!"
    hosts = sys.argv[1]
    for host in IPNetwork(hosts):
        server = getBanner(host)
        checkBanner(server,host)
    for i in range(len(windowsList)):
        print "%s : %s" %(windowsList[i][0], windowsList[i][1])
    time_stop = time.time()
    print "time: %.3f s" %(time_stop-time_start)
        
if __name__=="__main__":
	main()
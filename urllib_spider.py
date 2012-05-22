#!/usr/bin/env python
import urllib2
import os
import sys

keyword ='chenguangchen'
inputTime = 1412
header = {
 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0',
 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
 'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
# 'Accept-Encoding':'gzip, deflate',
 'DNT':'1',
# 'Connection':'keep-alive',
# 'Referer':'http://www.baidu.com/',
# 'Cookie':'BAIDUID=79741D75BB0E5D383F2D6FF9AE0827B6:FG=1; BDUT=rv3679741D75BB0E5D383F2D6FF9AE0827B613686caba690; BDREFER=%7Burl%3A%22http%3A//news.baidu.com/%22%2Cword%3A%22%22%7D; BDRCVFR[eHt_ClL0b_s]=mk3SLVN4HKm',
}

req = urllib2.Request(url=('http://www.baidu.com/s?wd=%s&rsv_bp=0&rsv_spt=3&inputT=%d'%(keyword,inputTime)),data=None,headers=header)

#get the first page 
content = urllib2.urlopen(req).read()

#search the page and locate left links



handler = open('urlsave.htm','wr')
handler.write(content)
handler.close()




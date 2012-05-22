#!/usr/bin/env python
import urllib2
import os
import sys

keyword ='chenguangchen'
inputTime = 1412

header_page0 = {
 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0',
 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
 'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
# 'Accept-Encoding':'gzip, deflate',
 'DNT':'1',
 'Connection':'keep-alive',
 'Referer':'http://www.baidu.com/',
 'Cookie':'BAIDUID=79741D75BB0E5D383F2D6FF9AE0827B6:FG=1; BDUT=rv3679741D75BB0E5D383F2D6FF9AE0827B613686caba690; BDREFER=%7Burl%3A%22http%3A//news.baidu.com/%22%2Cword%3A%22%22%7D; BDRCVFR[eHt_ClL0b_s]=mk3SLVN4HKm'
}

if __name__ == '__main__':
	curUrl = 'http://www.baidu.com/s?wd=%s&rsv_bp=0&rsv_spt=3&inputT=%d' %(keyword,inputTime)
	req = urllib2.Request(url=curUrl,data=None,headers=header_page0)
#get the first page 
	content = urllib2.urlopen(req).read()
	handler = open('urlsave0.htm','wr')
	handler.write(content)
	handler.close()
	lastUrl = curUrl

	curPage = 10
#get left pages ... 
	while (curPage < 100):
		header_pageX = {
		 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0',
		 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		 'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
#		 'Accept-Encoding':'gzip, deflate',
		 'DNT':'1',
		 'Connection':'keep-alive',
		 'Referer':lastUrl,
		 'Cookie':'BAIDUID=79741D75BB0E5D383F2D6FF9AE0827B6:FG=1; BDUT=rv3679741D75BB0E5D383F2D6FF9AE0827B613686caba690; BDREFER=%7Burl%3A%22http%3A//news.baidu.com/%22%2Cword%3A%22%22%7D; BDRCVFR[eHt_ClL0b_s]=mk3SLVN4HKm'
		}
		curUrl = 'http://www.baidu.com/s?wd=%s&pn=%d&usm=3' %(keyword,curPage)
		req = urllib2.Request(url=curUrl,data=None,headers=header_pageX)
		content = urllib2.urlopen(req).read()
		handler = open(('urlsave%d.htm' %(curPage/10)),'wr')
		handler.write(content)
		handler.close()
		lastUrl = curUrl
		curPage += 10
	else:
		print 'all %d pages downloaded' % (curPage/10)





#!/usr/bin/env python
#coding=utf-8

import urllib2
import urllib
import os
import sys
import time
#import codecs

in_encoding = sys.stdin.encoding
print 'in_encoding is '+str(in_encoding)
keyword = raw_input("input the keyword: ")
keyword = keyword.decode(in_encoding)

if len(sys.argv) is 2:
	maxpage = int(sys.argv[1])
else:
	maxpage = 30

#keyword must be encoded into 
#gbk or gb18030
kw_gbk = keyword.encode('gbk') 
kw_utf8 = keyword.encode('utf-8')
m1 = {'wd':kw_gbk}
m2 = {'wd':kw_utf8}

keyword_url1 = urllib.urlencode(m1)
keyword_url2 = urllib.urlencode(m2)
print 'keyword_url from gbk is:'+keyword_url1
print 'keyword_url from utf8 is:'+keyword_url2


header_page0 = {
 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0',
 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# 'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
# 'Accept-Encoding':'gzip, deflate',
 'DNT':'1',
 'Connection':'keep-alive',
 'Referer':'http://www.baidu.com/',
 'Cookie':'BAIDUID=79741D75BB0E5D383F2D6FF9AE0827B6:FG=1; BDUT=rv3679741D75BB0E5D383F2D6FF9AE0827B613686caba690; BDREFER=%7Burl%3A%22http%3A//news.baidu.com/%22%2Cword%3A%22%22%7D; BDRCVFR[eHt_ClL0b_s]=mk3SLVN4HKm'
	}


def check_nextPage(content,page):
	str1 = '<a href="s?%s&pn=%d">%d</a>' %(keyword_url1,page+10,(page/10)+2)
	print 'search string:%s' % str1
	if content.find(str1) == -1:
		print 'page%d is not exist'%(page/10+2)
		return False
	print 'page%d exist'%(page/10+2)
	return True

if __name__ == '__main__':	
	inputTime = 1120
	startT = time.clock()
#	curUrl = 'http://www.baidu.com/s?wd=%s&rsv_bp=0&rsv_spt=3&inputT=%d' %(keyword,inputTime)
#	Yes! must use keyword_url in below curUrl or urllib2.urlopen will report 
#	UnicodeEncodError
	curUrl = 'http://www.baidu.com/s?%s&rsv_bp=0&rsv_spt=3&inputT=%d' %(keyword_url2,inputTime) 
	req = urllib2.Request(url=curUrl,data=None,headers=header_page0)
#get the first page 
	content = urllib2.urlopen(req).read()
	handler = open('urlsave_all.htm','w')
	str_result = content
	lastUrl = curUrl
	curPage = 10
	isNextPageExist = True
#get left pages ... 
	while (curPage < maxpage * 10 and isNextPageExist == True):
		header_pageX = {
		 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0',
		 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#		 'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
#		 'Accept-Encoding':'gzip, deflate',
		 'DNT':'1',
		 'Connection':'keep-alive',
		 'Referer':lastUrl,
		 'Cookie':'BAIDUID=79741D75BB0E5D383F2D6FF9AE0827B6:FG=1; BDUT=rv3679741D75BB0E5D383F2D6FF9AE0827B613686caba690; BDREFER=%7Burl%3A%22http%3A//news.baidu.com/%22%2Cword%3A%22%22%7D; BDRCVFR[eHt_ClL0b_s]=mk3SLVN4HKm'
		}
		curUrl = 'http://www.baidu.com/s?%s&pn=%d' %(keyword_url2,curPage) #&usm=3
		req = urllib2.Request(url=curUrl,data=None,headers=header_pageX)
		content = urllib2.urlopen(req).read()

		if check_nextPage(content,curPage) == False:
			isNextPageExist = False

		str_result += '''<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="100%" color=#987cb9 SIZE=3>'''
		str_result += content
		lastUrl = curUrl
		curPage += 10
	else:
		print 'all %d pages downloaded (app let max download page be %d)' % (curPage/10,maxpage)
	

	endT = time.clock()
	print 'total time used %.2f seconds' % endT
	handler.write(str_result)
	handler.close()



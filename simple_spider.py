#!/usr/bin/env python
import sys
import socket
import os
import urllib,urllib2

tails1 = '''
Host: mirrors.163.com
User-Agent: Python-urllib/1.17

'''

tails2 = '''
Host: mirrors.163.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
DNT: 1
Connection: keep-alive
Referer: http://mirrors.163.com/.help/ubuntu.html
Cookie: vjuids=1e02f6cd0.1331a031732.0.f18cda6deb286; vjlast=1318991370.1337132187.11; _ntes_nnid=6b3cbc05ba2c1aa567d95332d28e61df,1337229628078; _ntes_nuid=6b3cbc05ba2c1aa567d95332d28e61df; P_INFO=mse_wlyq@126.com|1337230932|2|mail126|00&99|shh&1337229284&mail126#shh&null#10#0|&0; NTES_REPLY_NICKNAME=sgyhunter%40126.com%7Csgyhunter%7C3167796069646846314%7C8097099790%7Chttp%3A%2F%2Fmimg.126.net%2Fp%2Fbutter%2F1008031648%2Fimg%2Fface_big.gif%7C%7C1%7C2; ALLYESID4=00111103164514914412267; locOfCh=east; isGd=0; isFs=0; USERTRACK=116.228.28.82.1335241351366866; Province=021; City=021

'''

tails_baidu = '''HTTP/1.1
Host: www.baidu.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
DNT: 1
Connection: keep-alive
Referer: http://www.baidu.com/
Cookie: BAIDUID=79741D75BB0E5D383F2D6FF9AE0827B6:FG=1; BDUT=rv3679741D75BB0E5D383F2D6FF9AE0827B613686caba690; BDREFER=%7Burl%3A%22http%3A//news.baidu.com/%22%2Cword%3A%22%22%7D; BDRCVFR[eHt_ClL0b_s]=mk3SLVN4HKm

'''

def copy2file(buf,handler):
	handler.write(buf)

if __name__ == '__main__':
	print 'in main route'
	handler = open('savefile.html','wr')
	print "hello world,I am %s" % sys.argv[0]
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(("www.baidu.com",80))
	print "connect from",s.getsockname()
	print "connect to",s.getpeername()

	keyword='maozedong'

	try:
		s.sendall("GET /s?wd=%s&rsv_bp=0&rsv_spt=3&inputT=44924 %s" %(keyword,tails_baidu))
	except socket.error,e:
		print "error sending data: %s" % e
		sys.exit(1)

	while 1:
		try:
			buf = s.recv(2048)
		except socket.error,e:
			print "error receiving data:%s" % e
			sys.exit(1)
		if not len(buf):
			break
		copy2file(buf,handler)

	handler.close()
	sys.exit(0)




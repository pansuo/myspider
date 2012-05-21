import urllib2
import os
import sys

handler = open('urlsave.htm','wr')
keyword='maozedong'
content = urllib2.urlopen('http://www.baidu.com/s?wd=%s&rsv_bp=0&rsv_spt=3&inputT=1000' % keyword).read()

handler.write(content)

handler.close()




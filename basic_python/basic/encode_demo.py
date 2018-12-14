#!/usr/bin/python
# coding=utf-8

import sys
import chardet

# 返回当前系统所使用的默认字符编码

print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
# print sys.getdefaultencoding()

print "是的".decode("utf-8")

print u"是"

print '\xE7\x9F\xAD\xE5\xAF\xBF'.decode("utf-8")

s1 = '\xE7\x9F\xAD\xE5\xAF\xBF'.decode("utf-8")

print type(s1)

print s1
# t1 = '\\xE7\\x9F\\xAD\\xE5\\xAF\\xBF'.replace("\\", "\\")

t = '\xE7\x9F\xAD\xE5\xAF\xBF'
print type(u"中文")
print type('中文')
print "\xE5\x90\x8D\xE5\xAD\x97"
# print type(t)
# print t
# print "/".replace("/","\ ")

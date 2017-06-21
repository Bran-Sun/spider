# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import os

page = 1
url = 'http://www.qiushibaike.com/hot/page' + str(page)
usr_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5)'
headers = { 'User-Agent': usr_agent}

try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response.read(), "lxml")
    content = soup.find_all("div",class_="content")
    for x in content:
        print(x.get_text())

except urllib2.URLError, e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)

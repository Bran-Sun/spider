# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import os

class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.pagecount = 0
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5)'
        self.headers = { 'User-Agent' : self.user_agent }
        self.story = []
        self.enable = False

    def getPage(self, pageIndex):
        try:
            url = "http://www.qiushibaike.com/hot/page/" + str(pageIndex)
            request = urllib2.Request(url, headers = self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            r3eturn pageCode
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print(u"连接失败", e.reason)
                return None

    def get(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        soup = BeautifulSoup(response.read(), "lxml")
        content = soup.find_all("div",class_="content")
        self.pagecount += 1
        for x in content:
            self.story.append(x.get_text())

        return self.story

    def loadPage(self):
        if self.enable == True:
            if len(self.pagecount) < 2:
                pageS

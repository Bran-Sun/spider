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
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print(u"连接失败", e.reason)
                return None

    def getItem(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        soup = BeautifulSoup(pageCode, "lxml")
        content = soup.find_all("div",class_="content")
        pageStory = []
        for x in content:
            if x.get_text()!= '\n':
                pageStory.append(x.get_text())

        return pageStory

    def loadPage(self):
        if self.enable == True:
            if self.pagecount < 2:
                pageStory = self.getItem(self.pageIndex)
                if pageStory:
                    self.story.append(pageStory)
                    self.pageIndex += 1
                    self.pagecount += 1

    def getOneStory(self, pageStory, page):
        for story in pageStory:
            input = raw_input()
            self.loadPage()
            if input == "Q":
                self.enable = False
                return
            print(story)

    def start(self):
        print(u"正在读取糗事百科")
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if self.pagecount > 0:
                pageStory = self.story[0]
                nowPage += 1
                del self.story[0]
                self.pagecount -= 1
                self.getOneStory(pageStory, nowPage)

spider = QSBK()
spider.start()

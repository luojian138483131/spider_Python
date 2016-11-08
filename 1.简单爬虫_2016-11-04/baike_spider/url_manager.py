#coding=utf-8
class UrlManager(object):

    #带爬取的URL  已爬取得URL
    def __init__(self):

        self.old_urls = set()
        self.new_urls = set()
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    #批量添加URL
    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)#单个添加

    #判断是否新的URL
    def has_new_url(self):
        return len(self.new_urls) != 0
    #获取一个带爬取URL
    def get_new_url(self):
        new_url = self.new_urls.pop() #pop()获取并且移除URL
        self.old_urls.add(new_url)
        return new_url


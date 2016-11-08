#coding=utf-8
from baike_spider import html_parser
from baike_spider import html_downloader
from baike_spider import html_outputer
from baike_spider import url_manager





class SpoderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()

        self.downloder = html_downloader.HtmlDownloader()

        self.parser = html_parser.HtmlParser()

        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):#调度程序
        self.urls.add_new_url(root_url)
        #打印第几个URL
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d:%s'%(count,new_url)
                html_cont = self.downloder.download(new_url)
                #解析
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 10:
                    break

                count = count + 1

            except Exception as f:

                print 'craw failed:',f




        self.outputer.out_html()


if __name__=="__main__":
    root_url ="http://baike.baidu.com/view/21087.htm"
    obj_spider = SpoderMain()
    obj_spider.craw(root_url)


#coding=utf-8

#解析器
import re
import urlparse
from bs4 import BeautifulSoup
class HtmlParser(object):




    def _get_new_urls(self, page_url, soup):
        new_urls = set()#存储到列表
        #/view/123.htm
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))#正则表达式
        for link in links:
            new_url = link['href']
            #获取完整URL
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_data(self, page_url, soup):
        #存储数据
        res_data = {}
          #url
        res_data['url'] = page_url

        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        #<div class="lemma-summary"
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        #创建soup对象
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

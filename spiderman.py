from dataoutput import DataOutput
from htmldownloader import Htmldownloader
from htmlparser import HtmlParser
from urlmanager import UrlManager

class Spiderman(object):

    def __init__(self):
        self.manage = UrlManager()
        self.parser = HtmlParser()
        self.downloader = Htmldownloader()
        self.output = DataOutput()

    def crawl(self,root_url):
        self.manage.add_new_url(root_url)
        print(len(self.manage.new_urls))
        while(self.manage.has_new_url() and self.manage.old_url_size() < 100):
            try:
                new_url = self.manage.get_new_url()
                html = self.downloader.download(new_url)
                new_urls,data = self.parser.parser(new_url,html)
                self.manage.add_new_urls(new_urls)
                self.output.store_data(data=data)
                print('已经抓取%s个链接' % self.manage.old_url_size())
            except:
                print('crawl Failed')
        self.output.output_html()

if __name__ == '__main__':
    spider_man = Spiderman()
    spider_man.crawl('https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB')

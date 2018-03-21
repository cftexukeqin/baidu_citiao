# coding:utf-8
import re
import urllib.parse
from bs4 import BeautifulSoup as bs

class HtmlParser(object):

    def parser(self,page_url,html_content):
        if page_url is None or html_content is None:
            return
        soup = bs(html_content,'lxml')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_datas(page_url,soup)

        return new_urls,new_data

    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r'/item/%\w+'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_datas(self,page_url,soup):
        data = {}
        data['url'] = page_url
        title = soup.select('.lemmaWgt-lemmaTitle-title h1')[0].text
        data['title'] = title
        summary = soup.find('div',class_='lemma-summary')
        data['summary'] = summary.text

        return data



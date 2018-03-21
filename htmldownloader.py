# coding:utf-8

import requests

class Htmldownloader(object):
    def download(self,url):
        if url is None:
            return None
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
        headers = {'User-Agent':user_agent}
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            res.encoding = 'utf-8'
            return res.text
        return None
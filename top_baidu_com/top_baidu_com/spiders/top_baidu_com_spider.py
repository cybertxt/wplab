import scrapy
#import os

from top_baidu_com.items import TopBaiduComItem

class TopBaiduComSpider(scrapy.Spider):
    name = "TopBaiduCom"
    allowed_domains = ["baidu.com"]
    #print os.getcwd()
    start_urls = ["http://top.baidu.com/"]

    def parse(self, response):
        urls = response.xpath('//a[contains(@href, "http://")]/@href').extract()
        urls = [ url for url in set(urls) if url.find('&wd=') >= 0 ]
        for url in urls:
            item = TopBaiduComItem()
            item['url'] = url
            yield item

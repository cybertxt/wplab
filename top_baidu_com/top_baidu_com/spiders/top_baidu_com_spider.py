import scrapy

from top_baidu_com.items import TopBaiduComItem

class TopBaiduComSpider(scrapy.Spider):
    name = "TopBaiduCom"
    allowed_domains = ["baidu.com"]
    start_urls = ["http://top.baidu.com/"]

    def parse(self, response):
        urls = response.xpath('//a[contains(@href, "http://")]/@href').extract()
        urls = list(set(urls))
        for url in urls:
            item = TopBaiduComItem()
            item['url'] = url
            yield item

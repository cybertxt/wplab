import os
import json
import scrapy

from search_baidu_com.items import SearchBaiduComItem

class SearchBaiduComSpider(scrapy.Spider):
    name = "SearchBaiduCom"
    allowed_domains = ["baidu.com"]
    url_json = open('top.json', 'r').read()
    json_obj = json.loads(url_json)
    start_urls = []
    for urldict in json_obj:
        start_urls.append(urldict['url'])
	start_urls.reverse()

    def parse(self, response):
        item = SearchBaiduComItem()
        item['href'] = response.xpath('//div[@id="9"]//h3/a/@href').extract()[0]
        item['keyword'] = response.xpath('/html/head/title/text()').extract()[0][:-5]
        titlewords = response.xpath('//div[@id="9"]//h3/a//text()').extract()
        title = ''
        for t in titlewords:
            title += t
        item['title'] = title
        contentwords = response.xpath('//div[@id="9"]//div[@class="c-abstract"]//text()').extract()
        content = ''
        for c in contentwords:
            content += c
        item['content'] = content
        yield item

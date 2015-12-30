Linux Nginx PHP WordPress 
=========================

Installation
------------
Steps:
* Install nginx
* Install mysql
* Install php php-fpm php-xmlrpc php-mysql
* pip install python-wordpress-xmlrpc
* Create database for wordpress
* Create mysql user for wordpress
* Grant privileges to wp database on wp user
* Download wordpress and configure it to access mysql database
* Configure nginx

Scrapy
------
```
* start urls: http://top.baidu.com
* urls = response.xpath('//a[contains(@href, "http://")]/@href').extract()
* urls = list(set(urls)) # de-dup
* urls_json=json.dumps(urls) # to json
* scrapy crawl TopBaiduCom -o TopBaiduCom.json
```

Baidu Search Results
--------------------
```
* response.xpath('//div[contains(@id,"1")]/h3/a/@href').extract()
* href = response.xpath('//div[contains(@id,"1")]//h3/a[1]/@href').extract()[0]
* title = response.xpath('/html/head/title/text()').extract()[0][:-5]
```

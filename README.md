Linux Nginx PHP WordPress 
=========================

Installation
------------
Steps:
* Install nginx
* Install php php-fpm php-xmlrpc
* Install mysql
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

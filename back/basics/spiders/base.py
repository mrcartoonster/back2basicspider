# -*- coding: utf-8 -*-
import scrapy


class BaseSpider(scrapy.Spider):
    name = "base"
    start_urls = ["https://lifehacker.com/c/back-to-basics/"]

    def parse(self, response):
        """
        Parser for traversing the back-to-basics site.
        """
        articles = response.xpath('//div[@class="cw4lnv-5 aoiLP"]')
        for a in articles:
            yield {
                'h': a.xpath('./a/@href').get()
            }
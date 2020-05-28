# -*- coding: utf-8 -*-
import scrapy


class BaseSpider(scrapy.Spider):
    name = "base"
    start_urls = ["http://https://lifehacker.com/c/back-to-basics/"]

    def parse(self, response):
        """
        Parser for traversing the back-to-basics site.
        """
        pass

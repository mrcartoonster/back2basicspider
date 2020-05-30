# -*- coding: utf-8 -*-
import scrapy


class BaseSpider(scrapy.Spider):
    name = "base"
    start_urls = ["https://lifehacker.com/c/back-to-basics/"]

    def parse(self, response):
        """
        Parser for traversing the back-to-basics site.
        """
        articles = response.xpath('/html/body/div[3]/div[4]/main/div/div[4]/article[1]/div[3]/div/div[2]/a')
        for href in articles:
            yield response.follow(href, callback=self.parsing)
        # yield response.follow_all(articles, callback=self.parsing)

# -*- coding: utf-8 -*-
import scrapy


class BaseSpider(scrapy.Spider):
    name = "base"
    start_urls = ["https://lifehacker.com/c/back-to-basics/"]

    def parse(self, response):
        """
        Parser for traversing the back-to-basics site.
        """
        articles = response.xpath('//div[@class="cw4lnv-5 aoiLP"]/a')
        #   for href in articles:
        #       yield response.follow(href, callback=self.parsing)
        yield response.follow_all(articles, callback=self.parsing)

        page = response.xpath('//div[@class="qsfpej-0 bIkJGf"]/a')
        for href in page:
            yield response.follow(herf, callback=self.parse)

    def parsing(self, response):
        """
        Parsing first article from within posts.
        """
        arts = response.xpath(
            "/html/body/div[3]/div[5]/main/div/div[2]/div[2]"
        )

        for art in arts:
            yield {art.xpath("./p[1]/text()").get()}

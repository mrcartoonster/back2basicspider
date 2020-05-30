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
        for href in articles:
            yield response.follow(href, callback=self.parsing)

    def parsing(self, response):
        """
        Parsing first paragraph.
        """
        para = response.xpath(
            '//div[@class="r43lxo-0 hEDDLA js_post-content"]'
        )

        for p in para:
            yield {
                "para": p.xpath("./p[1]/text()").get(),
                "title": p.xpath(
                    '//header[@class="sc-1efpnfq-1 hQgdUv"]/h1/a/text()'
                ).get(),
            }

# -*- coding: utf-8 -*-
import scrapy
from basics.items import BasicsItem
from scrapy.loader import ItemLoader


class BaseSpider(scrapy.Spider):
    """Prime spider for for getting titles and first paragraph."""

    name = "base"
    start_urls = ["https://lifehacker.com/c/back-to-basics/"]

    def parse(self, response):
        """Parser for traversing the back-to-basics site."""
        articles = response.xpath('//div[@class="cw4lnv-5 aoiLP"]/a')
        for href in articles:
            yield response.follow(href, callback=self.parsing)

    def parsing(self, response):
        """Parse first paragraph."""
        para = response.xpath(
            '//div[@class="r43lxo-0 hEDDLA js_post-content"]'
        )

        for p in para:
            loader = ItemLoader(item=BasicsItem(), selector=p)
            loader.add_xpath(
                "title",
                '//header[@class="sc-1efpnfq-1 hQgdUv"]/h1/a/text() |\
                //h1[@class="gkv9lo-4 eNOFiQ"]/a/text() |\
                //a[@class="sc-1out364-0 hMndXN js_link"]/h1/text()',
            )
            response.xpath('//div[@class="sc-1mep9y1-0 sc-1ixdk2y-0 gclRUW"]')
            loader.add_xpath(
                "author",
                '//div[@class="sc-1mep9y1-0 sc-1ixdk2y-0 gclRUW"]'
            )
            loader.add_xpath("para", "./p[1]/text()")
            yield loader.load_item()

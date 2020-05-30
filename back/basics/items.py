# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


class BasicsItem(scrapy.Item):
    """Items will be the title of post, author and the first paragraph."""

    title = scrapy.Field(
        input_processor=MapCompose(remove_tags), output_processor=TakeFirst()
    )
    author = scrapy.Field(
        input_processor=MapCompose(remove_tags), output_processor=TakeFirst()
    )
    para = scrapy.Field(
        input_processor=MapCompose(remove_tags), output_processor=Join()
    )

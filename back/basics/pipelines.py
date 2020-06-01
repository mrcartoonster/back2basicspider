# -*- coding: utf-8 -*-
from databases import Database
from scrapy.exceptions import DropItem


class BasicsPipeline:
    """Pipeline to drop authors that are not Beth Skwarecki or Claire Lower."""

    def __init__(self, database):
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(database=crawler.settings.get("DB_URI"))

    async def open_spider(self, spider):
        self.db = await database.connect()

    async def close_spider(self, spider):
        self.db = await database.disconnect()

    def process_item(self, item, spider):
        """Check to see if author is in our list."""
        if item.get("author") in ["Beth Skwarecki", "Claire Lower"]:
            return item

        else:
            raise DropItem("Not the authors we want.")

# -*- coding: utf-8 -*-
from databases import Database
from sqlalchemy.engine.url import URL

from .models import basics
from .settings import DB_URI


class BasicsPipeline:
    """Pipeline to drop authors that are not Beth Skwarecki or Claire Lower."""

    def __init__(self, db_uri):
        self.db_uri = db_uri

    @classmethod
    def from_crawler(cls, crawler):
        return cls(db_uri=crawler.settings.get("DB_URI"))

    async def open_spider(self, spider):
        self.database = Database(self.db_uri)
        await self.database.connect()

    async def process_item(self, item, spider):
        query = basics.insert()
        await self.database.execute(query=query, values=item)
        return item

    async def close_spider(self, spider):
        await self.database.disconnect()

# -*- coding: utf-8 -*-
from typing import Any

from databases import Database

from .models import basics
from .settings import DB_URI


class BasicsPipeline:
    """
    Pipeline to drop authors that are not Beth Skwarecki or Claire Lower as
    well as inserting authors name, article title and first paragrapg into
    Postgres database.
    """

    database = None

    def __init__(self, db_uri):

        """
        Will change this using dataclasses once inserting items into Postgres
        database is successful.
        """
        self.db_uri = db_uri

    @classmethod
    def from_crawler(cls, crawler):

        """
         Scrapy crawler object to retreive database URL and database
         model from settings.py.
         """
        return cls(db_uri=crawler.settings.get("DB_URI"),)

    async def open_spider(self, spider):

        """Asyncio database connection."""
        self.database = Database(self.db_uri)
        await self.database.connect()

    async def close_spider(self, spider):

        """
        Asyncio database disconnect. Will create an async context block once
        able to insert items into Postgres database.
        """
        await self.database.disconnect()

    async def process_item(self, item, spider):
        query = basics.insert()
        await self.database.execute(query=query, values=item)
        return item

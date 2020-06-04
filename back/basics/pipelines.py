# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Any
from databases import Database
from sqlalchemy.engine.url import URL

from .models import basics
from .settings import DB_URI



@dataclass
class BasicsPipeline:
    """
    Pipeline to drop authors that are not Beth Skwarecki or Claire Lower as
    well as inserting authors name, article title and first paragrapg into
    Postgres database.
    """

    database: Any = Database(DB_URI)
    #   def __init__(self, database):
    #       """
    #       Will change this using dataclasses once inserting items into Postgres
    #       database is successful.
    #       """
    #       # self.db_uri = db_uri
    #       self.database = Database(DB_URI)

    #   @classmethod
    #   def from_crawler(cls, crawler):
    #       """
    #       Scrapy crawler object to retereive database URL and database
    #       model from settings.py.
    #       """
    #       return cls(
    #           db_uri=crawler.settings.get("DB_URI"),
    #       )

    async def open_spider(self, spider):
        """Asyncio database connection."""
        await database.connect()

    async def process_item(self, item, spider):
        query = basics.insert()
        await database.execute(query=query, values=item)
        return item

    async def close_spider(self, spider):
        """
        Asyncio database disconnect. Will create an async context block once
        able to insert items into Postgres database.
        """
        await database.disconnect()


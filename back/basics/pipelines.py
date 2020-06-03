# -*- coding: utf-8 -*-
from databases import Database
from models import basics
from sqlalchemy.engine.url import URL
# from scrapy.exceptions import DropItem
from settings import DATABASE

class BasicsPipeline:
    """Pipeline to drop authors that are not Beth Skwarecki or Claire Lower."""

    # Uncomment and integrate once your get database insertion working!
    #   def process_item(self, item, spider):
    #       """Check to see if author is in our list."""
    #       if item.get("author") in ["Beth Skwarecki", "Claire Lower"]:
    #           return item

    #       else:
    #           raise DropItem("Not the authors we want.")

    def process_item(self, item, spider):
        """Database pipeline insertion with Encode databases."""

        database = Database(URL(DATABASE), ssl=True)

        await database.connect()

        query = notes.insert()
        await database.execute(query=query, values=item)

        await database.disconnect()
        return item

# -*- coding: utf-8 -*-
from databases import Database
from models import basics
from scrapy.exceptions import DropItem


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
        pass

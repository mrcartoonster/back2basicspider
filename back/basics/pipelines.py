# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem


class BasicsPipeline:
    """Pipeline to drop authors that are not Beth Skwarecki or Claire Lower."""

    def process_item(self, item, spider):
        """Check to see if author is in our list."""
        if item.get("author") in ["Beth Skwarecki", "Claire Lower"]:
            return item

        else:
            raise DropItem("Not the author we want.")

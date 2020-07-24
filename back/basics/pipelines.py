# -*- coding: utf-8 -*-
from dataclasses import dataclass

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


@dataclass
class BasicsPipeline:
    """Pipeline to drop authors that are not Beth Skwarecki or Claire Lower."""

    ids_seen = set()

    def process_item(self, item, spider):
        """Check to see if author is in our list."""
        adapter = ItemAdapter
        if adapter.get("author") in ["Beth Skwarecki", "Claire Lower"]:
            self.ids_seen.add(adapter.get("author"))
            return item
        else:
            raise DropItem("Not the author we want.")

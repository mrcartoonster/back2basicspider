# -*- coding: utf-8 -*-
# Sample customer logger from scrapy example: https://doc.scrapy.org/en/latest/topics/logging.html#custom-log-formats
import logging

from scrapy.logformatter import LogFormatter

CRAWLEDMSG = "Crawled (%(status)s) %(request)s%(request_flags)s (referer: %(referer)s)%(response_flags)s"


class CrawlLog(LogFormatter):
    def crawled(self, request, response, spider):
        """Logs a message when the crawler finds a webpage."""
        request_flags = " %s" % str(request.flags) if request.flags else ""
        response_flags = " %s" % str(response.flags) if response.flags else ""
        return {
            "level": logging.DEBUG,
            "msg": CRAWLEDMSG,
            "args": {
                "status": response.status,
                "request": request,
                "request_flags": request_flags,
                "referer": referer_str(request),
                "response_flags": response_flags,
                # backward compatibility with Scrapy logformatter below 1.4 version
                "flags": response_flags,
            },
        }

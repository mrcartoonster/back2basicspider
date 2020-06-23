# Sample customer logger from scrapy example: https://doc.scrapy.org/en/latest/topics/logging.html#custom-log-formats
from scrapy.logformatter import LogFormatter


class PoliteLogFormatter(LogFormatter):
    """
    Simple logger to overide severity of dropped items.
    """

    def dropped(self, item, exception, response, spider):
        """Using LogFormatter dropped method."""

        return {
            'level': logging.INFO,  # lowering the level from logging.WARNING.
            'msg': "Dropped: %(exceptions)s" + os.linesep + "%(item)s",
            'args': {
                'exception': exception,
                'item': item,
            }
        }

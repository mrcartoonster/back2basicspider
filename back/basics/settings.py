# -*- coding: utf-8 -*-
import os
from pathlib import Path

import pendulum as p
from confidential import SecretsManager
from .loggers.politelogger import PoliteLogFormatter

confidential = SecretsManager(
    secrets_file_default=(
        "/home/mrnobody/projects/back2basicspider/.confidential/default.json"
    ),
    secrets_file=os.environ.get("SECRETS_FILE"),
    region_name="us-east-1",
)


BOT_NAME = "basics"

SPIDER_MODULES = ["basics.spiders"]
NEWSPIDER_MODULE = "basics.spiders"

LOG_LEVEL = "INFO"
LOG_FILE = Path() / "logs.txt"
LOG_DATEFORMAT = p.now().format("L" * 4)
LOG_FORMAT = '%(asctime)s [%(name)s]i %(levelname)s %(lineno)d: %(message)s'
LOG_FORMATTER = PoliteLogFormatter

DB_URI = confidential["DB_URI"]
DEPTH_STATS_VERBOSE = True
USER_AGENT = "basics (mrcartoonster@gmail.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = .63
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#  'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'basics.middlewares.BasicsSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'basics.middlewares.BasicsDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

ITEM_PIPELINES = {
    "basics.pipelines.BasicsPipeline": 300,
    "scrapy.pipelines.images.ImagesPipeline": 1,
    "scrapy.pipelines.files.FilesPipeline": 1,
}

IMAGES_STORE = str(Path("images/").absolute())
FILES_STORE = str(Path("files/").absolute())
IMAGES_THUMBS = {
    "small": (50, 50),
    "big": (270, 270),
}
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# UTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See #httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 10
HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

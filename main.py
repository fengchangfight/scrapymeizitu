import sys
import os
sys.path.append(os.getcwd())

from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from meizitu.spiders.MeizituLinkSpider import MeizituLinkSpider
from meizitu.spiders.MeizituSpider import MeizituSpider

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner(get_project_settings())
d = runner.crawl(MeizituSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run()
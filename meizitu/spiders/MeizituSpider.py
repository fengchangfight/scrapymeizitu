import scrapy
import os; print(os.getcwd())
from scrapy.spiders import CrawlSpider
from meizitu.items import MeizituItem
from meizitu.util.xpathutil import XpathUtil


class MeizituSpider(CrawlSpider):
    name = "meizitu"
    start_urls = ['http://www.meizitu.com/a/280.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'meizitu.pipelines.ImagesDownloadPipeline.ImagesDownloadPipeline': 1
        }
    }

    def parse(self, response):
        item = MeizituItem()
        item['image_urls'] = response.xpath('.//div[@id="maincontent"]/descendant::*/img/@src').extract()
        # go to the next page, call back should be parse itself
        yield item

import os; print(os.getcwd())
from scrapy.spiders import CrawlSpider
from meizitu.items import MeizituItem
from meizitu.util.MongoUtils import MongoUtils


class MeizituSpider(CrawlSpider):
    name = "meizitu"

    start_urls = MongoUtils.findAllLinks(MongoUtils.create_client().meizitu)

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

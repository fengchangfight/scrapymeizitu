import scrapy
import os; print(os.getcwd())
from scrapy.spiders import CrawlSpider
from meizitu.items import MeizituLinkItem
from meizitu.util.xpathutil import XpathUtil


class MeizituLinkSpider(CrawlSpider):
    name = "meizitulink"
    start_urls = ['http://www.meizitu.com/a/more_1.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'meizitu.pipelines.LinkSaverPipeline.LinkSaverPipeline': 1
        }
    }

    def parse(self, response):
        wpItems = response.xpath("//" + XpathUtil.xpath_for_class('wp-item'))
        for wpItem in wpItems:
            item = MeizituLinkItem()
            item['url'] = ''.join(wpItem.xpath(".//descendant::*/a[1]/@href").extract_first())
            yield  item
        nextpage = ''.join(response.xpath('//div[@id="wp_page_numbers"]/descendant::*/li[last()-1]/a/@href').extract())
        yield scrapy.Request(response.urljoin(nextpage))





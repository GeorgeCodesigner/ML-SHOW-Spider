from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from sz_housing_price.items import SzHousingPriceItem
from sz_housing_price.spiders.szDistrict import szDistrict
from scrapy.http import Request
import re

class sz_housing_price(CrawlSpider):
    name = 'sz_housing_price'
    start_urls = ['http://esf.sz.fang.com/house-a090-b0352/i31/']

    def parse(self,response):
        item = SzHousingPriceItem()
        disKey=response.url.split("/")[-3]

        selector = Selector(response)
        area = selector.xpath('//dd/div[2]/p[1]/text()').extract()
        price = selector.xpath('//dd/div[3]/p[1]/span[1]/text()').extract()

        item['area']=area
        item['price']=price
        item['disKey']=disKey
        yield item

        baseUrl = 'http://esf.sz.fang.com/'  # 房天下网站上二手房信息深圳的baseUrl
        district = szDistrict()
        dist = district.getDistrict()
        urls=[]
        for key in dist:
            if dist[key]=='buji':
                for pindex in range(2, 11):
                    urls.append(baseUrl + key + 'i3' + str(pindex) + '/')
            else:
                for pindex in range(1, 11):
                    urls.append(baseUrl + key + 'i3' + str(pindex) + '/')

        for url in urls:
            yield Request(url, callback=self.parse)

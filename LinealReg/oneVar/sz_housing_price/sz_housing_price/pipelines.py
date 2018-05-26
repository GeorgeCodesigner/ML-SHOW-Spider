# -*- coding: utf-8 -*-

# Define your item pipelines here
# re.findall(r"\d+",item['area'][i])
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sz_housing_price.spiders.szDistrict import szDistrict
import re

class SzHousingPricePipeline(object):
    def process_item(self, item, spider):
        # print(item)
        district = szDistrict()
        dist = district.getDistrict()
        for key in dist:
            if item['disKey']==key.split("/")[-2]:
                fp = open('需要保存文件的绝对路径' + dist[key] + '.txt', 'a+')
                arr_len=len(item['area'])
                for i in range(0,arr_len):
                    areaNum=re.findall(r"^\d+",item['area'][i])[0]
                    fp.write(str(areaNum) + ',')
                    fp.write(item['price'][i] + '\n')

        return item

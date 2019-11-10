# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeishijieItem(scrapy.Item):
    # define the fields for your item here like:
    chengpin = scrapy.Field()
    gongyi = scrapy.Field()
    kouwei = scrapy.Field()
    nandu = scrapy.Field()
    renshu = scrapy.Field()
    zhunbeishijian = scrapy.Field()
    pengrenshijian = scrapy.Field()
    zhuliao = scrapy.Field()
    fuliao = scrapy.Field()
    guocheng = scrapy.Field()

    pass

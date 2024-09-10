# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HhScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    company = scrapy.Field()
    solary = scrapy.Field()
    _id = scrapy.Field()
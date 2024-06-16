# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 表示要保存的數據，類似ORM
class EbookItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    date = scrapy.Field()
    describe = scrapy.Field()
    source = scrapy.Field()
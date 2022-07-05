# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FormClickerItem(scrapy.Item):
    date = scrapy.Field()
    login = scrapy.Field()
    answer = scrapy.Field()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_relationship_nets = scrapy.Field()
    pass


class User_InfoItem(scrapy.Item):
    user_info = scrapy.Field()
    pass


class Article_InfoItem(scrapy.Item):
    article_info = scrapy.Field()
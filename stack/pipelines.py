# -*- coding: utf-8 -*-

# Define your item pipelines here
#
import pymongo
from scrapy.utils.project import get_project_settings
settings = get_project_settings()
from scrapy.exceptions import DropItem
import logging


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            logging.log(logging.DEBUG, "Question added to MongoDB database!")
        return item
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class StackPipeline:
    def process_item(self, item, spider):
        return item

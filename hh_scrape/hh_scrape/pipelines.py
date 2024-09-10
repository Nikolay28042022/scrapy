# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient

class HhScrapePipeline:
    def __init__(self) -> None:
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vacancies100924

    def process_item(self, item, spider):
        # Добавляем каждый элемент (данные с вакансий) в список

        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item



# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

# 可以將數據保存到SQLite數據庫中
# 要在Scrapy中使用這個Pipeline，需要將它添加到settings.py文件中的ITEM_PIPELINES設置中

class SQLitePipeline(object):

    def open_spider(self, spider):
        self.connection = sqlite3.connect('../ebook.db')
        self.c = self.connection.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS eBook (
                id INTEGER NOT NULL UNIQUE,
                url TEXT,
                title TEXT,
                category TEXT,
                date TEXT,
                describe TEXT,
                source TEXT,
                PRIMARY KEY(id)
            )
        ''')
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO eBook (url, title, category, date, describe, source) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', 
            (item.get('url'),
            item.get('title'),
            item.get('category'),
            item.get('date'),
            item.get('describe'),
            item.get('source'))
        )
        self.connection.commit()
        return item
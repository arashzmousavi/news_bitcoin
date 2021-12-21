# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from typing import Counter
import sqlite3


class NewsPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("news.db")
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""DROP TABLE IF EXISTS news""")
        self.cur.execute("""CREATE TABLE news(
                        time TEXT,
                        title TEXT,
                        description TEXT
                        )""")

    def process_item(self, item, spider):
        self.store(item)
        return item

    def store(self, item):
        self.cur.execute("""INSERT INTO news VALUES (?,?,?)""", (
            item['time'],
            item['title'],
            item['description']
        ))
        self.conn.commit()

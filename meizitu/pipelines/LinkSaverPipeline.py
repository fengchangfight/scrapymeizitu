from pymongo import MongoClient

class LinkSaverPipeline(object):
    # ==fc== init sql client
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/meizitu")
        self.db = self.client.meizitu
        self.bulk = self.db.links.initialize_ordered_bulk_op()

    # ==fc== write into db article
    def process_item(self, article, spider):
        stripped_links = {
            "url": article["url"]
        }
        self.bulk.insert(stripped_links)
        return article

    # ==fc== execute and close connection to mysql
    def close_spider(self, spider):
        result = self.bulk.execute()
        print("Link write result:")
        print(result)
        self.client.close()

# -*- coding: utf-8 -*-
import requests
from scrapy.conf import settings
import os,pymongo


class CosplayPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODE_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_DOCNAME"]

        client = pymongo.MongoClient(host=host, port=port)

        mydb = client[dbname]

        self.sheet = mydb[sheetname]


    def process_item(self, item, spider):
        if 'image_urls' in item:
            images = []
            dir_path = './Images'
            # print dir_path
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            for image_url in item['image_urls']:
                us = image_url.split('/')[3:]
                image_file_name = '_'.join(us)
                file_path = '%s/%s' % (dir_path, image_file_name)
                images.append(file_path)
                if os.path.exists(file_path):
                    continue

                with open(file_path, 'wb') as handle:
                    response = requests.get(image_url, stream=True)
                    for block in response.iter_content(1024):
                        if not block:
                            break

                        handle.write(block)

            item['images'] = images

        data = dict(item)
        self.sheet.insert(data)
        return item
# -*- coding: utf-8 -*-
import requests
from Cosplay import settings
import os,json,codecs


class CosplayPipeline(object):
    def process_item(self, item, spider):
        if 'image_urls' not in item:
            images = []
            for image_url in item['image_urls']:
                # us = image_url.split('/')[3:]
                # image_file_name = '_'.join(us)
                image_file_name = image_url.split('/')[-1]
                dir_path = '%s/%s' % (settings.IMAGES_STORE,image_url.split('/')[4])
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                file_path = '%s/%s' % (dir_path,image_file_name)
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
        return item

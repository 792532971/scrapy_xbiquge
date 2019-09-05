# -*- coding: utf-8 -*-
import os
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class XiaoshuoPipeline(object):
    def process_item(self, item, spider):
        return item


class FictionPipeline(object):

    def process_item(self, item, spider):
        curPath = 'D:\新笔趣阁小说'
        tempPath = str(item['name'])
        targetPath = curPath + os.path.sep + tempPath
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)

        filename_path = 'D:\新笔趣阁小说' + os.path.sep + str(item['name']) + os.path.sep + str(item['chapter_name']) + '.txt'
        with open(filename_path, 'w', encoding='utf-8') as f:
            f.write(item['content'] + "\n")
            return item

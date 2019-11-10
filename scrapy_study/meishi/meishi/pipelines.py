# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import csv
import logging


class MeishijiePipeline(object):

    def __init__(self):
        meishijie = os.path.dirname(__file__) + '/data/result.csv'
        print(meishijie)
        print("*************************初始化文件输出**********************************")
        # 打开文件
        self.file_of_lawyer_list = open(meishijie, 'a+', encoding="utf-8", newline='')
        # 定义写入的writer
        self.lawyer_list_writer = csv.writer(self.file_of_lawyer_list, dialect='excel')

    def process_item(self, item, spider):
        logging.info("====>写出数据到文件")
        self.lawyer_list_writer.writerow([
            item['chengpin'],
            item['gongyi'],
            item['kouwei'],
            item['nandu'],
            item['renshu'],
            item['zhunbeishijian'],
            item['pengrenshijian'],
            item['zhuliao'],
            item['fuliao']
        ])
        self.file_of_lawyer_list.flush()
        return item

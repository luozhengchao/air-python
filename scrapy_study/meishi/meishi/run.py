import subprocess
import schedule
import time
from scrapy import cmdline

if __name__ == '__main__':
    args = "scrapy crawl meishi".split()
    cmdline.execute(args)

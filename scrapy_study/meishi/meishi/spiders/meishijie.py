import scrapy
from scrapy_study.meishi.meishi.items import MeishijieItem

"""本爬虫用于爬取美食杰网站"""


class MeishiSpider(scrapy.Spider):
    name = "meishi"
    # allowed_domains=["http://www.meishij.net"]
    # 起始url
    start_urls = [
        # 首页："http://www.meishij.net/chufang/diy/wucan/?&page=1"
        # 生成多页(这里设置为10页)：
        "http://www.meishij.net/chufang/diy/wucan/?&page=%d" % (i + 1) for i in range(1)
    ]

    # 首页爬取方法：抽取详细页面的链接
    def parse(self, response):
        # 获取详细页面
        hrefs = response.xpath("//div[@class='listtyle1']/a")
        for href in hrefs:
            # 抽取详细页面连接
            url = href.xpath("@href")[0].extract()
            # print(url)
            # 解析详细页面
            yield scrapy.Request(url, callback=self.parse_detail_page)

    # 具体页面爬取方法：人工定位各个信息的位置
    def parse_detail_page(self, response):
        # 选择抓取结构
        info2 = response.xpath("//div[@class='info2']")
        item = MeishijieItem()
        # # 获取成品图(链接)
        item['chengpin'] = response.xpath("//div[@class='cp_headerimg_w']/img/@src")[0].extract()
        # 获取工艺
        item['gongyi'] = (info2.xpath("//li[@class='w127']/a").xpath("text()").extract() + [''])[0]
        # 获取口味
        item['kouwei'] = (info2.xpath("//li[@class='w127 bb0']/a").xpath("text()").extract() + [''])[0]
        # 获取难度
        item['nandu'] = (info2.xpath("//li[@class='w270']//a").xpath("text()").extract() + [''])[0]
        # 获取人数
        item['renshu'] = (info2.xpath("//li[@class='w270 br0']//a").xpath("text()").extract() + [''])[0]
        # 获取准备时间
        item['zhunbeishijian'] = (info2.xpath("//li[@class='w270 bb0']//a").xpath("text()").extract() + [''])[0]
        # 获取烹饪时间
        item['pengrenshijian'] = (info2.xpath("//li[@class='w270 bb0 br0']//a").xpath("text()").extract() + [''])[0]
        # 获取主料
        item['zhuliao'] = dict()
        for h4 in response.xpath("//div[@class='yl zl clearfix']//h4"):
            item['zhuliao'][h4.xpath("a/text()").extract()[0]] = h4.xpath("span/text()").extract()[0]
        # # 获取辅料
        item['fuliao'] = dict()
        for li in response.xpath("//div[@class='yl fuliao clearfix']//li"):
            item['fuliao'][li.xpath("h4/a/text()").extract()[0]] = li.xpath("span/text()").extract()[0]
        # # 获取过程（文本+链接）
        # # 当前步数
        count = 0
        # item['guocheng'] = dict()
        # for div in response.xpath("//div[@class='editnew edit']/div/div"):
        #     count += 1
        #     item['guocheng'][count] = (div.xpath("p/text()")[0].extract(), div.xpath("p/img/@src")[0].extract())

        yield item

# -*- coding: utf-8 -*-
import scrapy
from xiaoshuo.items import XiaoshuoItem


class XbiSpider(scrapy.Spider):
    name = 'xbi'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/xiaoshuodaquan/']

    def parse(self, response):
        lis = response.xpath("//div[@id='main']//li")
        for li in lis:
            url = li.xpath(".//a/@href").get()
            yield scrapy.Request(url, callback=self.parse_two)

    # 章节页面
    def parse_two(self, response):
        name = response.xpath("//h1/text()").get().strip()
        lists = response.xpath("//div[@id='list']/dl/dd/a/@href").extract()
        for list in lists:
            yield scrapy.Request(url=response.urljoin(list), meta={"name": name}, callback=self.parse_detail)

    # 内容页面
    def parse_detail(self, response):
        # 小说名字
        name = response.meta['name']
        # 章节名字
        chapter_name = response.xpath("//h1/text()").get()
        # 章节内容
        content = response.xpath("//div[@id='content']//text()").getall()
        content = "".join(content)
        yield XiaoshuoItem(name=name, chapter_name=chapter_name, content=content)




import scrapy


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ["https://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
        filename = "teacher.html"
        open(filename,'wb').write(response.body)
        pass

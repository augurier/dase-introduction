import scrapy


class DdSpider(scrapy.Spider):
    name = "dd"
    allowed_domains = ["dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.54.00.00.00.00.html"]

    def parse(self, response):
        url_all = ["http://category.dangdang.com/pg{}-cp01.54.00.00.00.00.html".format(i) for i in range(2,101)]
        filename = "cs_all.html"
        open(filename,'wb').write(response.body)
        for i in url_all:
            yield scrapy.Request(url=i, callback=self.parse_text, dont_filter=True)
        pass

    def parse_text(self,response):
        filename = "cs_all.html"
        open(filename,'ab').write(response.body)
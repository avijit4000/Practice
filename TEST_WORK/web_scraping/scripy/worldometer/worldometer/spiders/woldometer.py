import scrapy


class WoldometerSpider(scrapy.Spider):
    name = "woldometer"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        pass

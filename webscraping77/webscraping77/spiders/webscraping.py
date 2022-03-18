import scrapy


class WebscrapingSpider(scrapy.Spider):
    name = 'webscraping'
    start_urls = ['https://www.redeloteria.com.br/']

    def parse(self, response):
        for mega in response.css('.numberCircleMega'):
            yield{
                'resultado': response.css('.numberCircleMega::text').getall()
            }

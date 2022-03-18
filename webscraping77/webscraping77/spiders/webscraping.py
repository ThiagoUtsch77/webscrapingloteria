import scrapy


class WebscrapingSpider(scrapy.Spider):
    name = 'webscraping'
    start_urls = ['https://www.redeloteria.com.br/']


    def parse(self, response):

            yield{
                'Mega-Sena': response.css('h2:nth-child(6)::text').getall(),
                'Resultado': response.css('.numberCircleMega::text').getall()
            }
            yield{
                'Lotofacil': response.css('h2:nth-child(11)::text').getall(),
                'Resultado': response.css('.numberCircleLotoFacil::text').getall()
            }
            yield{
                'Quina': response.css('h2:nth-child(16)::text').getall(),
                'Resultado': response.css('.numberCircleQuina::text').getall()
            }
            yield {
                'Lotomania': response.css('h2:nth-child(21)::text').getall(),
                'Resultado': response.css('.numberCircleLotoMania::text').getall()
            }
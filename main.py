# date: 2017.12.10
# https://stackoverflow.com/a/47744135/1832058

import scrapy

#from allegro.items import AllegroItem

#class AllegroItem(scrapy.Item):
#    product_name = scrapy.Field()
#    product_sale_price = scrapy.Field()
#    product_seller = scrapy.Field()

class OlxPrices(scrapy.Spider):

    name = "OlxPrices"
    allowed_domains = ["olx.pl"]

    start_urls = [
        "https://www.olx.pl/elektronika/telefony/q-iphone-9/?search%5Border%5D=created_at:desc&search%5Bfilter_enum_state%5D%5B0%5D=used"
    ]

    def parse(self, response):
        title = response.xpath('//h6[@class="css-z3gu2d"]//text()').extract()
        sale_price = response.xpath('//p[@class="css-13afqrm"]//text()').extract()
        seller = response.xpath('//p[@class="css-1mwdrlh"]/a/span/text()').extract()

        title = title[0].strip()

        print(title, sale_price, seller)

        yield {'title': title, 'price': sale_price, 'seller': seller}

        #items = AllegroItem()
        #items['product_name'] = ''.join(title).strip()
        #items['product_sale_price'] = ''.join(sale_price).strip()
        #items['product_seller'] = ''.join(seller).strip()
        #yield items

# --- run it as standalone script without project and save in CSV ---

from scrapy.crawler import CrawlerProcess

#c = CrawlerProcess()

c = CrawlerProcess({
#    'USER_AGENT': 'Mozilla/5.0',
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'output.csv'
})

c.crawl(OlxPrices)
c.start()

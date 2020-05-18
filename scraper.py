import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://ishopchangiwines.com/spirits?product_list_limit=30&volume=349']

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import platform
platform.python_version()

import numpy as np
import pandas as pd
import re
import logging
import json
import scrapy
import re
import sys
import requests
#from pandas.io.json import json_normalize
from bs4 import BeautifulSoup
import os
import pickle
from scrapy.crawler import CrawlerProcess

import scrapy
import requests


# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException


def clean(text):
    digits = [s for s in text if s.isdigit()]
    clean_text = ''.join(digits)
    if not clean_text:
        return None
    return int(clean_text)


class QuotesSpider(scrapy.Spider):
    name = "Wildberries"
    allowed_domains = ['wildberries.ru']
    start_urls = [
        'https://www.wildberries.ru/catalog/obuv/zhenskaya/sabo-i-myuli/myuli',

    ]

    custom_settings = {
        'LOG_LEVEL': logging.WARNING,
        'ITEM_PIPELINES': {'__main__.JsonWriterPipeline': 1},  # Used for pipeline 1
        'FEED_FORMAT': 'json',  # Used for pipeline 2
        'FEED_URI': 'quoteresult.json'  # Used for pipeline 2
    }

    # def parse(self, response):
    #     response.xpath("//div[@class='dtList i-dtList j-card-item ']/span[@class='text']").extract()
    #     for quote in response.css('.dtList i-dtList j-card-item '):
    #         time =  quote.css('div::attr(data-catalogercod1s)').extract()
    #         yield {'time':time,}

    def parse(self, response):
        for quote in response.css('.dtList-inner'):
            link = quote.css('.dtlist-inner-brand-name')
            title1 = link.css('.brand-name::text').get()
            title2 = link.css('.goods-name::text').get()
            title = title1 + '/' + title2

            catalogercod1s = quote.css('div::attr(data-catalogercod1s)').extract()
            raw_price = quote.css('.lower-price::text').get()
            id = quote.css('div::attr(id)').extract()
            image = quote.css('img::attr(src)').extract()
            price = raw_price and clean(raw_price) or None

            link = quote.css('a::attr(href)').extract()
            list_link = quote.css('a::attr(href)')
            for parselink in list_link:
                character = parselink.css('.comments_reviews_link > span > i').extract()

            size = quote.xpath('//div[@class="quick-order"]/span[@class="sizes"]/a[@rel="nofollow"]/text()').extract()

            yield {
                'title': title,
                'price': price,
                'id': id,
                'character': character,
                'timestamp': catalogercod1s,
                'link ': link,
                'size': size,
                'image': image,

            }

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(QuotesSpider)
process.start()
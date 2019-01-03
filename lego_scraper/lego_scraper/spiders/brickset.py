# -*- coding: utf-8 -*-
import scrapy


class BricksetSpider(scrapy.Spider):
    name = 'brickset'
    allowed_domains = ['brickset.com']
    start_urls = ['https://brickset.com/sets/year-2016']

    def parse(self, response):
        for brickset in response.css('article.set'):
            meta = brickset.css('div.meta')
            
            number = meta.css('h1 span::text').re_first(r'(.+): ')
           
            name = brickset.css('div.highslide-caption h1::text').extract_first()
            print(number, name)

            yield {
                'number': number,
                'name': name,
            }

        next_url = response.css('li.next a::attr(href)').extract_first()
        if next_url:
            yield scrapy.Request(next_url)

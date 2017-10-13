# -*- coding: utf-8 -*-
import scrapy


class MiguelpuigSpider(scrapy.Spider):
    name = "miguelpuig"
    allowed_domains = ["miguelpuig.com"]
    start_urls = ['http://miguelpuig.com/']

    def parse(self, response):
	    print response.body

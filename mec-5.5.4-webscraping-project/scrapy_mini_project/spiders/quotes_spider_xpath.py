import scrapy


class QuotesSpider(scrapy.Spider):
    name = "toscrape_xpath"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):

            yield {
                #    'text': quote.css('span.text::text').get(),
                'text': quote.xpath('span[@class="text"]/text()').get(),
                # 'author': quote.css('small.author::text').get(),
                'author': quote.xpath('span/small[@class="author"]/text()').get(),
                # 'tags': quote.css('div.tags a.tag::text').getall(),
                'tags': quote.xpath('div[@class="tags"]/a/text()').getall(),
            }

        # next_page = response.css('li.next a::attr(href)').get()
        next_page = response.xpath('//li[@class="next"]/a/@href').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

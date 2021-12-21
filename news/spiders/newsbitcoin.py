import scrapy
from ..items import NewsItem


class NewsSpider(scrapy.Spider):
    name = "newsbitcoin"
    start_urls = [
        "https://cointelegraph.com/tags/bitcoin",
        "https://www.moneycontrol.com/news/tags/cryptocurrency.html/news/"
        # "https://www.livebitcoinnews.com/"
    ]

    def parse(self, response):
        counter = NewsItem()

        for title in response.css("li.posts-listing__item"):
            counter["time"] = title.css(
                "time.post-card-inline__date::text").get()
            counter["title"] = title.css(
                "span.post-card-inline__title::text").get()
            counter["description"] = title.css(
                "p.post-card-inline__text::text").get()
            yield counter

        for title in response.css("li.clearfix"):
            counter["time"] = title.css("span::text").get()
            counter["title"] = title.css("h2 a::attr(title)").get()
            counter["description"] = title.css("p::text").get()
            yield counter

import scrapy

class TescoScraperMainItem(scrapy.Item):
    product_id = scrapy.Field()
    product_url = scrapy.Field()
    image_url = scrapy.Field()
    product_title = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
    product_description = scrapy.Field()
    name_and_address = scrapy.Field()
    return_address = scrapy.Field()
    net_contents = scrapy.Field()

class TescoScraperReviewItem(scrapy.Item):
    product_id = scrapy.Field()
    review_title = scrapy.Field()
    stars_count = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    review_text = scrapy.Field()

class TescoScraperUsuallyBoughtNextProducts(scrapy.Item):
    product_id = scrapy.Field()
    product_url = scrapy.Field()
    product_title = scrapy.Field()
    product_image_url = scrapy.Field()
    price = scrapy.Field()

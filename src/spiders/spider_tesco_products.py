from scrapy import Request
from scrapy import Spider
from  src.items.item_tesco  import  TescoScraperMainItem, TescoScraperUsuallyBoughtNextProducts, TescoScraperReviewItem
from src.xpath.xpath_tesco import XPATH_PRODUCTS_URLS, XPATH_IMAGE_URL,  XPATH_PRODUCT_TITLE, XPATH_CATEGORY, XPATH_PRICE,  \
    XPATH_PRODUCT_DESCRIPTION, XPATH_NAME_AND_ADDRESS, XPATH_RETURN_ADDRESS, XPATH_NET_CONTENTS, XPATH_PRODUCT_USUALLY_BOUGHT_URL, \
    XPATH_PRODUCT_USUALLY_BOUGHT_TITLE, XPATH_PRODUCT_USUALLY_BOUGHT_IMAGE_URL, XPATH_PRODUCT_USUALLY_BOUGHT_PRICE, \
    XPATH_PAGINATION_BUTTONS, XPATH_PRODUCT_USUALLY_BOUGHT_LIST, XPATH_REVIEW_COUNT, XPATH_REVIEW_SHOW_MORE_TEXT, XPATH_REVIEW_LIST, \
    XPATH_REVIEW_TITLE, XPATH_REVIEW_STARS_COUNT, XPATH_REVIEW_AUTHOR, XPATH_REVIEW_DATE, XPATH_REVIEW_TEXT_1, XPATH_REVIEW_TEXT_2, XPATH_REVIEW_SHOW_MORE_LINK

class TescoSpider(Spider):
    name = "tesco"
    useragent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
    start_urls = []
    connection = None

    def __init__(self, **kwargs):
        self.start_urls = kwargs.get('start_urls', [])
        self.connection = kwargs.get('connection', None)

    def parse(self, response):
        pagionations_buttons_list = [button.attrib.get('href', None) for button in  response.xpath(XPATH_PAGINATION_BUTTONS)]
        for product_url in response.xpath(XPATH_PRODUCTS_URLS):
            request_main = response.follow(product_url.attrib.get('href', ''), self.parse_tesco_main)
            yield request_main
        if  pagionations_buttons_list[-1]:
            #yield Request(response.urljoin(TescoSpider.base_url + pagionations_buttons_list[-1]), self.parse)
            yield response.follow(pagionations_buttons_list[-1], self.parse)

    def parse_review(self, response):
        tesco_product_id_cleared = int(response.url.split('products/')[1].split('?')[0])
        for review in response.xpath(XPATH_REVIEW_LIST):
            review_title = review.xpath(XPATH_REVIEW_TITLE).get()
            review_stars_count = review.xpath(XPATH_REVIEW_STARS_COUNT).get()
            review_author = review.xpath(XPATH_REVIEW_AUTHOR).get()
            review_date = review.xpath(XPATH_REVIEW_DATE).get()
            review_text_1 = review.xpath(XPATH_REVIEW_TEXT_1).get()
            if review_text_1:review_text = review_text_1
            else:review_text = review.xpath(XPATH_REVIEW_TEXT_2).get()

            try:
                review_stars_count_cleared = int(''.join([s for s in review_stars_count if s.isdigit()]))
            except:
                review_stars_count_cleared = None

            tesco_review_item = TescoScraperReviewItem()
            tesco_review_item['product_id'] = tesco_product_id_cleared
            tesco_review_item['review_title'] = review_title
            tesco_review_item['stars_count'] = review_stars_count_cleared
            tesco_review_item['author'] = review_author
            tesco_review_item['date'] = review_date
            tesco_review_item['review_text'] = review_text
            yield tesco_review_item
        show_more_link = response.xpath(XPATH_REVIEW_SHOW_MORE_LINK).get()
        if show_more_link:
            request_view = response.follow(show_more_link, self.parse_review)
            yield request_view

    def parse_tesco_main(self, response):
        tesco_product_id = response.url.split('/')[-1]
        tesco_product_url = response.url
        tesco_product_image_url = response.xpath(XPATH_IMAGE_URL).extract_first()
        tesco_product_title = response.xpath(XPATH_PRODUCT_TITLE).extract_first()
        tesco_product_category = '/'.join(response.xpath(XPATH_CATEGORY).getall())
        tesco_product_price = response.xpath(XPATH_PRICE).get()
        tesco_product_description = ' '.join(response.xpath(XPATH_PRODUCT_DESCRIPTION).getall())
        tesco_product_name_and_address = ','.join(response.xpath(XPATH_NAME_AND_ADDRESS).getall())
        tesco_product_return_address = ','.join(response.xpath(XPATH_RETURN_ADDRESS).getall())
        tesco_product_net_content = ','.join(response.xpath(XPATH_NET_CONTENTS).getall())

        tesco_product_id_cleared = int(tesco_product_id)
        tesco_product_price_cleared = float(tesco_product_price) if tesco_product_price else None

        tesco_product_item = TescoScraperMainItem()
        tesco_product_item['product_id'] = tesco_product_id_cleared
        tesco_product_item['product_url'] = tesco_product_url
        tesco_product_item['image_url'] = tesco_product_image_url
        tesco_product_item['product_title'] = tesco_product_title
        tesco_product_item['category'] = tesco_product_category
        tesco_product_item['price'] = tesco_product_price_cleared
        tesco_product_item['product_description'] = tesco_product_description
        tesco_product_item['name_and_address'] = tesco_product_name_and_address
        tesco_product_item['return_address'] = tesco_product_return_address
        tesco_product_item['net_contents'] = tesco_product_net_content

        yield tesco_product_item

        for bought in response.xpath(XPATH_PRODUCT_USUALLY_BOUGHT_LIST):
            tesco_usually_bought_product_id = tesco_product_id_cleared
            tesco_product_usually_bought_url = bought.xpath(XPATH_PRODUCT_USUALLY_BOUGHT_URL).get()
            tesco_product_usually_bought_title = bought.xpath(XPATH_PRODUCT_USUALLY_BOUGHT_TITLE).get()
            tesco_product_usually_bought_image_url = bought.xpath(XPATH_PRODUCT_USUALLY_BOUGHT_IMAGE_URL).get()
            tesco_product_usually_bought_price = bought.xpath(XPATH_PRODUCT_USUALLY_BOUGHT_PRICE).get()

            tesco_product_usually_bought_price_cleared = float(tesco_product_usually_bought_price) if tesco_product_usually_bought_price else None

            tesco_usually_bought_item = TescoScraperUsuallyBoughtNextProducts()
            tesco_usually_bought_item['product_id'] = tesco_usually_bought_product_id
            tesco_usually_bought_item['product_url'] = response.url + tesco_product_usually_bought_url
            tesco_usually_bought_item['product_title'] = tesco_product_usually_bought_title
            tesco_usually_bought_item['product_image_url'] = tesco_product_usually_bought_image_url
            tesco_usually_bought_item['price'] = tesco_product_usually_bought_price_cleared
            yield tesco_usually_bought_item

        for review in response.xpath(XPATH_REVIEW_LIST):
            review_title = review.xpath(XPATH_REVIEW_TITLE).get()
            review_stars_count = review.xpath(XPATH_REVIEW_STARS_COUNT).get()
            review_author = review.xpath(XPATH_REVIEW_AUTHOR).get()
            review_date = review.xpath(XPATH_REVIEW_DATE).get()
            review_text_1 = review.xpath(XPATH_REVIEW_TEXT_1).get()
            if review_text_1:review_text = review_text_1
            else:review_text = review.xpath(XPATH_REVIEW_TEXT_2).get()

            try:
                review_stars_count_cleared = int(''.join([s for s in review_stars_count if s.isdigit()]))
            except:
                review_stars_count_cleared = None

            tesco_review_item = TescoScraperReviewItem()
            tesco_review_item['product_id'] = tesco_product_id_cleared
            tesco_review_item['review_title'] = review_title
            tesco_review_item['stars_count'] = review_stars_count_cleared
            tesco_review_item['author'] = review_author
            tesco_review_item['date'] = review_date
            tesco_review_item['review_text'] = review_text
            yield tesco_review_item
        show_more_link = response.xpath(XPATH_REVIEW_SHOW_MORE_LINK).get()
        if show_more_link:
            request_view = response.follow(show_more_link, self.parse_review)
            yield request_view








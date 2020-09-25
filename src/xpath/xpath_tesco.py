#Pagination
XPATH_PAGINATION_NEXT_PAGE = '//a[@class="pagination--button prev-next"]'
XPATH_PAGINATION_LAST_PAGE = '//a[@class="pagination--button prev-next disabled"]'
XPATH_PAGINATION_BUTTONS = '//nav//a[contains(@class, "prev-next")]'

#Product page
XPATH_PRODUCT_LIST = '//ul[@class="product-list grid"]//li'
XPATH_PRODUCTS_URLS= '//ul[@class="product-list grid"]//li//div[@class="product-details--content"]//h3/a'
XPATH_PRODUCT_ID = '//ul[@class="product-list grid"]//li//div[@class="tile-content"]/@data-auto-id'
XPATH_IMAGE_URL = '//div[@class="product-image__container"]/img/@src'
XPATH_PRODUCT_TITLE= '//div[@class="product-details-tile__title-wrapper"]//h1/text()'
XPATH_CATEGORY = '//div[@class="breadcrumbs"]//span/text()'
XPATH_PRICE = '//div[@class="product-details-tile__main"]//div[@class="price-control-wrapper"]//span[@class="value"]/text()'
XPATH_PRODUCT_DESCRIPTION = '(//h2[contains(@class,"product-info-block__title")])//preceding::ul[@class="product-info-block__content"]//text()'
XPATH_NAME_AND_ADDRESS = '//div[@id="manufacturer-address"]//ul//text()'
XPATH_RETURN_ADDRESS = '//div[@id="return-address"]//ul//text()'
XPATH_NET_CONTENTS = '//div[@id="net-contents"]//p/text()'

#Review
XPATH_REVIEW_COUNT = '//div[@id="review-data"]//section[@class="primary-text"]//h4//text()'
XPATH_REVIEW_SHOW_MORE_TEXT = '//span[contains(@class, "beans-link__text") and contains(text(), "more reviews")]//text()'
XPATH_REVIEW_SHOW_MORE_LINK = '//span[contains(text(), "more reviews")]/parent::*/@href'
XPATH_REVIEW_LIST = '//div[@data-auto="review-list-container"]//article[@class="content"]/section'
XPATH_REVIEW_TITLE = './/h4//text()'
XPATH_REVIEW_STARS_COUNT = './/div[contains(@class, "beans-star-rating__container")]/span//text()'
XPATH_REVIEW_AUTHOR = '(.//p)[1]//text()'
XPATH_REVIEW_DATE = './/span[@class="submission-time"]//text()'
XPATH_REVIEW_TEXT_1 = '(.//p)[3]//text()'
XPATH_REVIEW_TEXT_2 = '(.//p)[2]//text()'


#Usually Bought Next Products
XPATH_PRODUCT_USUALLY_BOUGHT_LIST = '(//div[@class="recommender__wrapper"]//div[@class="product-tile-wrapper"])'
XPATH_PRODUCT_USUALLY_BOUGHT_URL = './/div[@class="tile-content"]//a[@class="product-image-wrapper"]/@href'
XPATH_PRODUCT_USUALLY_BOUGHT_TITLE = './/div[@class="product-details--content"]//text()'
XPATH_PRODUCT_USUALLY_BOUGHT_IMAGE_URL = './/div[@class="product-image__container"]//img[@class="product-image"]/@src'
XPATH_PRODUCT_USUALLY_BOUGHT_PRICE = './/div[@class="price-details--wrapper"]//span[@data-auto="price-value"]/text()'
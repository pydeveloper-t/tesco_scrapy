from src.items.item_tesco import TescoScraperMainItem, TescoScraperUsuallyBoughtNextProducts, TescoScraperReviewItem
from src.database.models.tesco_products import TescoProducts
from src.database.models.tesco_bought_next import TescoBoughtNext
from src.database.models.tesco_reviews import TescoReviews
class TescoScraperPipeline:
    def process_item(self, item, spider):
        if isinstance(item, TescoScraperMainItem):
            return self.handleProduct(item, spider)
        elif isinstance(item, TescoScraperUsuallyBoughtNextProducts):
            return self.handleUsuallyBoughtNextProducts(item, spider)
        elif isinstance(item, TescoScraperReviewItem):
            return self.handleReviewItem(item, spider)

    def handleProduct(self, item, spider):
        row = TescoProducts(**item)
        spider.connection.session.add(row)
        #print(f'MAIN {item}')

    def handleUsuallyBoughtNextProducts(self, item, spider):
        row = TescoBoughtNext(**item)
        spider.connection.session.add(row)
        #print(f'UsuallyBoughtNextProducts {item}')

    def handleReviewItem(self, item, spider):
        row = TescoReviews(**item)
        spider.connection.session.add(row)
        #print(f'ReviewItem {item}')

    def close_spider(self, spider):
        spider.connection.session.commit()
        spider.connection.session.close()

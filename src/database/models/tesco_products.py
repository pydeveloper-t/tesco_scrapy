from src.database import Base
from sqlalchemy import Column, Integer, String, DECIMAL, Text

class TescoProducts(Base):
    __tablename__ = 'tesco_products'
    product_id = Column(Integer, primary_key=True)
    product_url = Column(String(2048))
    image_url = Column(String(2048))
    product_title = Column(String(4096))
    category = Column(String(1024))
    price = Column(DECIMAL(10, 2))
    product_description = Column(Text)
    name_and_address = Column(Text)
    return_address = Column(Text)
    net_contents = Column(Text)

    def __init__(self, **kwargs):
        self.product_id = kwargs['product_id']
        self.product_url = kwargs['product_url']
        self.image_url = kwargs['image_url']
        self.product_title = kwargs['product_title']
        self.category = kwargs['category']
        self.price = kwargs['price']
        self.product_description = kwargs['product_description']
        self.name_and_address = kwargs['name_and_address']
        self.return_address = kwargs['return_address']
        self.net_contents = kwargs['net_contents']

    def __repr__(self):
        return "<Data %s, %s>" % (self.id, self.product_title)
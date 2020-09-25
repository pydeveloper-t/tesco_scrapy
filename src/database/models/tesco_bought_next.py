from src.database import Base
from sqlalchemy import Column, Integer, String, DECIMAL, Text


class TescoBoughtNext(Base):
    __tablename__ = 'tesco_bought_next'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer)
    product_url = Column(String(2048))
    product_title = Column(String(4096))
    product_image_url = Column(String(2048))
    price = Column(DECIMAL(10,2))

    def __init__(self, **kwargs):
        self.product_id = kwargs['product_id']
        self.product_url = kwargs['product_url']
        self.product_title = kwargs['product_title']
        self.product_image_url = kwargs['product_image_url']
        self.price = kwargs['price']

    def __repr__(self):
        return "<Data %s, %s>" % (self.id, self.product_title)
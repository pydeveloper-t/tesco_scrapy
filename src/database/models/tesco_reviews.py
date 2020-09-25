from src.database import Base
from sqlalchemy import Column, Integer, String, Text

class TescoReviews(Base):
    __tablename__ = 'tesco_reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer)
    review_title = Column(String(2048))
    stars_count = Column(Integer)
    date = Column(String(64))
    review_text = Column(Text)

    def __init__(self, **kwargs):
        self.product_id = kwargs['product_id']
        self.review_title = kwargs['review_title']
        self.stars_count = kwargs['stars_count']
        self.date = kwargs['date']
        self.review_text = kwargs['review_text']

    def __repr__(self):
        return "<Data %s, %s, %s>" % (self.id, self.product_id, self.review_title)
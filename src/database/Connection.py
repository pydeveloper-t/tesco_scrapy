import os
from src.database import Base
from src.database.models.tesco_bought_next import TescoBoughtNext
from src.database.models.tesco_products import TescoProducts
from src.database.models.tesco_reviews import TescoReviews
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connection:
    def __init__(self):
        self.engine = self.db_connect()
        self.create_tables(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    @staticmethod
    def _get_connection_string():
        dbhost = os.getenv("DBHOST")
        dbuser = os.getenv("DBUSER")
        dbpassword = os.getenv("DBPASSWORD")
        dbport = os.getenv("DBPORT")
        dbbase = os.getenv("DBBASE")
        return  f'mysql+pymysql://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbbase}'

    def create_tables(self, engine):
        Base.metadata.create_all(self.engine)

    def db_connect(self):
        return create_engine(Connection._get_connection_string())


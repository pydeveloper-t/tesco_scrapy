# tesco_scrapy

The Scrapy based parser for crawling tesco.com



## Requirements

- Python 3.6
- MySQL 
- pipenv(pip)


## How to install?
- Install python 3.6 (https://www.python.org/downloads/release/python-360/)
- Install pipenv
```
	pip install  pipenv
```	
- Clone repo to local disk
```
	git clone https://github.com/pydeveloper-t/tesco_scrapy.git . 
```	
-  Installing all neccessary packages
```
    cd <project_folder>
    pipenv install --ignore-pipfile
```	





### Edit configuration file (.env)
Set the actual credentials for MySQL:  DBHOST, DBPORT, DBBASE, DBUSER, DBPASSWORD 
and path (absolute or relative) for storing log-files: LOGDIR and path to file with URLs list for scraping: URLS

```
URLS       = ./urls/tesco_urls
LOGDIR     = './Log'
DBHOST     = localhost
DBPORT     = 3306
DBBASE     = tesco
DBUSER     = xxxxxxxxxxx
DBPASSWORD = xxxxxxxxxxx

```

```
https://www.tesco.com/groceries/en-GB/shop/household/kitchen-roll-and-tissues/all
https://www.tesco.com/groceries/en-GB/shop/pets/cat-food-and-accessories/all
```

### Run spider
```
pipenv run  python ./start/run_tesco.py
```

  
### Additional Information
> Alembic a database migration toop used in this project for  perform migrations to handle changes to the database. (See https://alembic.sqlalchemy.org/en/latest/index.html)

```
alembic current
alembic revision --autogenerate -m "Description of migration"
alembic upgrade head
```


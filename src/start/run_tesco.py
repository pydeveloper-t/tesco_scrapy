import logging
import os, sys, errno
sys.path.insert(0, os.path.abspath(__file__ + "/../../../"))
from datetime import datetime
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from src.database.Connection import Connection
from scrapy.utils.project import get_project_settings
from src.spiders.spider_tesco_products import TescoSpider

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):pass
        else:raise

if __name__ == '__main__':
    urls_list_file = os.getenv("URLS")
    configure_logging(install_root_handler=False)
    log_dir = os.path.abspath(os.getenv("LOGDIR", os.path.join(SCRIPT_DIR, 'Log')))
    log_file_name = 'tesco_' + str(datetime.utcnow())[:19].replace('-', '').replace(':', '').replace(' ', '_') + '.log'
    mkdir_p(log_dir)
    logging.basicConfig(
        filename=os.path.join(log_dir, log_file_name),
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )
    if urls_list_file:
        try:
            with open(urls_list_file, 'r') as f:
                start_urls = f.readlines()
        except Exception as exc:
            print(f'File {urls_list_file} open error: {exc}')
            raise SystemExit
        else:
            process = CrawlerProcess(get_project_settings())
            process.crawl(TescoSpider, start_urls=start_urls, connection=Connection() )
            process.start()
            process.stop()

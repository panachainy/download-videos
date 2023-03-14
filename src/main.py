from db.db import DB  # init_sqlite, save_link
from scraping import get_hls_link_from
import fire

dbClient = DB()


if __name__ == '__main__':
    fire.Fire(DB)


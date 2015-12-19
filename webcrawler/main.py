# -*- coding: utf-8 -*-

# 进入项目根目录
import os
project_path = os.path.split(os.path.realpath(__file__))[0]
os.chdir(project_path)

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from lib.music import MusicCrawler
from lib.book import BookCrawler
from lib.movie import TopMovieCrawler


if __name__ == '__main__':
    # crawler = MusicCrawler()
    # crawler.run()
    # BookCrawler().get_book_list('互联网')
    # BookCrawler().get_book_list('算法')

    TopMovieCrawler().get_top_movie_list("http://movie.douban.com/top250")

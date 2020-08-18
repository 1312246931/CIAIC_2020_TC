import requests
from bs4 import BeautifulSoup
import logging
import traceback
import numpy
import random
def init_logger(log_file=None):
    '''
    日志打印函数
    :param log_file: 日志文件输出地址
    :return:初始化后的日志器
    '''
    log_format = logging.Formatter("[%(asctime)s %(levelname)s] %(message)s")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.handlers = [console_handler]

    if log_file and log_file != '':
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)

    return logger
class Douban_Inquire():
    def __init__(self):

        pass
    pass
    def get_web_douban(self):
        info_all = []
        for page in range(0, 10):
            url = url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
            web_info_douban = Douban_Inquire.request_douban(self,url)
            soup = BeautifulSoup(web_info_douban, 'lxml')
            info1 = Douban_Inquire.save_to_excel(self,soup)
            info_all.append(info1)
            # print(info_all)
        return info_all
    def request_douban(self,url):
        headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'},
                   {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
                   {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
                   {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'},
                   {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
                   {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'},
                   {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'},
                   {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1'},
                   {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1'},
                   {'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},
                   {'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
                   {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'},
                   {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'},
                   {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36'},
                   {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'},
                   {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)'},
                   {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)'},
                   {'User-Agent': 'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124'}]
        try:
            response = requests.get(url, headers=headers[int(numpy.floor(len(headers) * random.random()))])
            if response.status_code == 200:
                return response.text
        except requests.RequestException:
            logger.info("服务器拒绝访问:"+str(response.status_code))
            return None

    def save_to_excel(self,soup):
        lists = soup.find(class_='grid_view').find_all('li')
        big_items = []
        for item in lists:
            item_name = item.find(class_='title').string
            item_img = item.find('a').find('img').get('src')
            #item_index = item.find(class_='').string
            item_score = item.find(class_='rating_num').string
            item_author = item.find('p').text
            item_link = item.find('a').get('href')
            if (item.find(class_='inq') != None):
                item_intr = item.find(class_='inq').string
            else:
                item_intr = '无'
            # print(' |电影名称: ' + item_name + ' |豆瓣评分:' + item_score + ' |豆瓣简介: ' + item_intr+'|主演：'+item_author+'|链接：'+item_img)
            items = [item_img, item_name, item_score, item_author, item_intr,item_link]
            pass
            big_items.append(items)
        return big_items


def init_logger(log_file=None):
    log_format = logging.Formatter("[%(asctime)s %(levelname)s] %(message)s")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.handlers = [console_handler]

    if log_file and log_file != '':
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)

    return logger

logger = init_logger(log_file=".\\0808.log")




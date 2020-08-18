import requests
from bs4 import BeautifulSoup
import xlwt
import logging


def request_douban(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '图片')
sheet.write(0, 2, '排名')
sheet.write(0, 3, '评分')
sheet.write(0, 4, '作者')
sheet.write(0, 5, '简介')

n = 1


def save_to_excel(soup):
    list = soup.find(class_='grid_view').find_all('li')

    for item in list:
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_score = item.find(class_='rating_num').string
        item_author = item.find('p').text
        if(item.find(class_='inq')!=None):
            item_intr = item.find(class_='inq').string
        else:
            item_intr='无'


        # try:
        #     item_intr = item.find(class_='inq').string
        # except AttributeError:
        #     item_intr = 'None'

        # if (item.find(class_='inq') != None):
        # if item.find(class_='inq'):
        #     item_intr = item.find(class_='inq').string

        # print('爬取电影：' + item_index + ' | ' + item_name +' | ' + item_img +' | ' + item_score +' | ' + item_author +' | ' + item_intr )
        print('爬取电影：' + item_index + ' |电影名称 ' + item_name + ' |豆瓣评分' + item_score + ' |豆瓣简介 ' + item_intr)

        global n

        sheet.write(n, 0, item_name)
        sheet.write(n, 1, item_img)
        sheet.write(n, 2, item_index)
        sheet.write(n, 3, item_score)
        sheet.write(n, 4, item_author)
        sheet.write(n, 5, item_intr)

        n = n + 1


def main(page):
    url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
    html = request_douban(url)

    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)


if __name__ == '__main__':

    for i in range(0,11):
        main(i)

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


book.save(u'豆瓣最受欢迎的250部电影.xlsx')

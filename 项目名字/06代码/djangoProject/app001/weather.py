import numpy
import random
import logging
import requests


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
logger=init_logger(log_file='./日志.log')

class WeatherGet:
    def __init__(self,url):
        url = 'http://www.weather.com.cn/weather15d/'+str(url)+'.shtml'
        self.url = url
        pass
    def request_weather_web(self,url):
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
                   {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}]
        try:
            response = requests.get(url, headers=headers[int(numpy.floor(len(headers) * random.random()))])
            response.encoding = 'gbk'
            response.encoding = 'utf-8'
            if response.status_code == 200:
                return response.text
        except requests.RequestException:
            logger.info('获取服务器数据错误：'+str(response.status_code))
            return None

    def get_weather_info(self,soup):

        lists = soup.find('ul', class_='t clearfix').find_all('li')
        weather_eightday = []
        for item in lists:
            try:  # 找到周几和具体几号
                item_date = item.find('span', class_='time').text
            except:
                item_date = '无'
            try:  # 得到具体的天气
                item_wea = item.find('span', class_='wea').text
            except:
                item_wea = '无'
            try:
                item_tem = item.find('span', class_='tem').text
            except:
                item_tem = '无'
            try:
                item_wind = item.find('span', class_='wind').text
            except:
                item_wind = '无'
            try:
                item_wind1 = item.find('span', class_='wind1').text
            except:
                item_wind1 = '无'
            logger.info('|日期：' + item_date + ' |天气' + item_wea + ' |温度' + item_tem+ ' |风向' + item_wind+ ' |风级' + item_wind1)
            weather_oneday = [item_date, item_wea, item_tem, item_wind, item_wind1]
            weather_eightday.append(weather_oneday)
        return weather_eightday

    def get_weather_surroundingregion(self,soup):
        weather_allcity = []
        item_region = soup.find('h1', class_='clearfix city').find('span').text
        item_update_time = soup.find('h1', class_='clearfix city').find('i').text
        lists = soup.find('ul', class_='clearfix city').find_all('li')
        m = 1
        for item in lists:
            try:  # 城市名
                item_city = item.find('span').text
            except:
                item_city = '无'
            try:  # 城市温度
                item_citytem = item.find('i').text
            except:
                item_citytem = '无'
            try:  # 城市天气网站链接
                item_city_list = item.find('a').get('href')
            except:
                item_city_list = '无'
            logger.info(
                '|城市：' + item_city + ' |温度' + item_citytem + ' |网站链接' + item_city_list )
            weather_city = [item_city, item_citytem, item_city_list]
            weather_allcity.append(weather_city)
            m = m + 1
        return weather_allcity


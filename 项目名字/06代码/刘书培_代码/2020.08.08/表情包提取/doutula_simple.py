#!C:\ProgramData\Anaconda3\python3.exe
# -*- coding: UTF-8 -*-

'''
@project:Pycharm
@file:doutula_simple.py
@author:Shupei Liu
@time: 2020/8/8 15:30
@mail: 1215235665@qq.com
'''

import requests
from bs4 import BeautifulSoup
import xlwt
import os
import re
import logging

def init_logger(log_file=None):
    #日志配置
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

def request_doutula(url):
    #验证网站是否能正常响应
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    #向访问网站提供你所使用的浏览器类型及版本、操作系统及版本、浏览器内核、等信息的标识
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        #如果网站能正常响应，则返回200，否则返回None
    except requests.RequestException:
        return None

def save_to_excel_and_download(sheet, soup, headers):
    #从网页编码中提取需要的信息保存在excel表格中
    list = soup.find(class_='col-sm-9 center-wrap').find_all(class_='list-group-item random_list tg-article')
    for item in list:

        list_1 = item.find(class_='random_article').find_all(class_='col-xs-6 col-sm-3')
        for item_1 in list_1:
            item_name = item.find(class_='random_title').text
            item_name = re.sub("[0-9-]", "", item_name)
            item_time = item.find(class_='random_title').find(class_='date').string
            item_img = item_1.find('img').get('data-original')
            if item_img is None:
                logger.error('None')
            #如果不存在item_img,则输出None
            else:
                logger.info('爬取表情包：' + item_name + '|'+ item_img)
                global n
                sheet.write(n, 0, item_name)
                sheet.write(n, 1, item_time)
                sheet.write(n, 2, item_img)
                download_pic(item_img, headers, item_name)
                n=n+1

def download_pic(item_img, headers, item_name):
    #下载从网页链接提取到的图片
    response = requests.get(item_img, headers=headers)
    data = response.content
    os.getcwd()
    os.makedirs(str(item_name), exist_ok=True)
    #生成一个目录
    file_path = "/" + str(item_name) + '/' + str(n) + ".png"
    with open(os.getcwd() + file_path, "wb") as f:
        f.write(data)
        logger.info("爬取图片+1")

logger = init_logger(log_file=os.path.join('C:/Users/LSP/Desktop/python学习笔记/表情包提取','extract_meme.log'))

def main(page, sheet, book):
    #主函数
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    url = 'http://www.doutula.com/article/list/?page='+str(page)
    ##################################
    html = request_doutula(url)
    soup = BeautifulSoup(html, 'lxml')
    #BeautifulSoup提取网页信息
    save_to_excel_and_download(sheet, soup, headers)
    book.save(u'表情包列表.xls')

def book_initialization():
    #要得到的excel表格中统计的图片信息，都是可以从网页编码提取到的信息比如表情包类别名、表情包发布时间、具体图片的网页链接
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('斗图啦套图', cell_overwrite_ok=True)
    sheet.write(0, 0, '名称')
    sheet.write(0, 1, '时间')
    sheet.write(0, 2, '图片')
    return sheet, book

if __name__ == '__main__':
    n = 1
    sheet, book = book_initialization()
    for i in range(1, 2):
        #需要爬的页码数
        main(i, sheet, book)

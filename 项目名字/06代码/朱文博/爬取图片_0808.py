#C:\user\zwb\PycharmProjects\test3
# -*- coding:UTF_8 -*-

'''
@project:Pycharm
@file:crawl_pic.py
@author:Wenbo Zhu
@time:2020/8/8 15:33

'''
import os
import urllib
import urllib.request
import urllib.parse
import urllib.error
import requests
from bs4 import BeautifulSoup
import xlwt
import urllib.request
import logging


def init_logger(log_file=None):
    '''
    初始化logger
    :param log_file: 存放日志的地址
    :return:初始化的logger
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


def download_img(img_url,headers,name):
    '''
    下载图片并保存
    :param img_url: 图片链接地址
    :param headers: 浏览器
    :param name: 图片保存的名字
    :return:图片名
    '''

    request = urllib.request.Request(img_url, headers=headers)
    try:
        response = urllib.request.urlopen(request)
        img_name = "img_%s.png"%(name)
        filename = os.path.join('E:\images',img_name)
        if (response.getcode() == 200):#如果响应代码为200则保存
            with open(filename, "wb") as f:
                f.write(response.read()) # 将内容写入图片
            return filename
    except:
        return "failed"


def soup_analysis(url,headers):
    '''
    用Beautiful soup 来拉取网页信息
    :param url: 网页地址
    :param headers: 浏览器
    :return:拉取后的信息
    '''
    response=requests.get(url,headers=headers)
    data=response.text
    soup=BeautifulSoup(data,'html.parser')
    print(soup)
    return soup


def create_sheet(title,label_name):
    '''
    创建一个execl表格
    :param title: 工作表名称
    :param label_name: 工作表列名称
    :return: 创建的execl、工作表
    '''
    pic_info=xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet=pic_info.add_sheet(title,cell_overwrite_ok=True)
    sheet.write(0,0,label_name[0])
    sheet.write(0,1,label_name[1])
    return pic_info,sheet


def add_sheet(img_ID,label1,label2,sheet):
    '''
    表格更新，记录图片信息
    :param img_ID: 图片ID
    :param label1: 第一类的名称
    :param label2: 第二类的名称
    :param sheet:  初始化后的工作表
    :return: 输入后的工作表
    '''
    sheet.write(img_ID, 0, label1)
    sheet.write(img_ID, 1, label2)
    img_ID += 1
    return sheet


def extract_info(big_class,big_keyword,small_class,label,soup,sheet,headers,img_ID):
    '''
    提取所需要的网页信息，一级一级得到所需要的标题以及图片链接
    :param big_class: 网页信息大类名称
    :param big_keyword: 网页信息大类关键词
    :param small_class: 网页信息小类名称
    :param label: 所要提取信息的名称
    :param soup: 拉取的网页信息
    :param sheet: 工作表
    :param headers: 浏览器
    :param img_ID: 图片ID
    :return: 更新后的工作表，更新后的图片ID
    '''
    imag_infos=soup.find_all(big_class,class_=big_keyword)
    for imag_info in imag_infos:
        small_class_imag_info=imag_info.find_all(small_class)
        for small_class_imag_info in small_class_imag_info:
            name=small_class_imag_info.get(label[0])
            link=small_class_imag_info.get(label[1])
            try:
                download_img(link, headers, img_ID)
                add_sheet(img_ID,name,link,sheet)
                img_ID+=1
                logger.info(img_ID)
                logger.info(name)
                logger.info(link)
            except ValueError:
                logger.error('error')
                continue
    return sheet,img_ID


def main(page,sheet_org,img_ID):
    '''
    主函数
    :param page: 图片的页数
    :param sheet_org: 原始工作表
    :param img_ID: 原始图片ID
    :return: 更新后工作表，更新后图片ID
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    url='http://soso.nipic.com/?q=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&g=1&or=0&y=48&page='+str(page)
    soup=soup_analysis(url,headers)
    big_class='li'
    big_keyword='new-search-works-item'
    small_class='img'
    label=['alt','data-original']
    sheet,img_ID=extract_info(big_class,big_keyword,small_class,label,soup,sheet_org,headers,img_ID)
    return sheet,img_ID


if __name__=='__main__':
    logger = init_logger(log_file=os.path.join('C:/Users/zwb/PycharmProjects/test3', 'qianghuang_tql.log'))

    sheet_title='pic_info'
    column_name=['标题','链接']
    pic_info,sheet_org=create_sheet(sheet_title,column_name)
    img_ID=1
    for page in range(3,5):
        sheet_org,img_ID=main(page,sheet_org,img_ID)
    pic_info.save(u'图片信息1.xlsx')














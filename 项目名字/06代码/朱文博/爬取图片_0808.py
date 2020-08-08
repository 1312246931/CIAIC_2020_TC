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

'''
初始化logger
'''
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


'''
下载图片并保存
'''
def download_img(img_url,headers,name):
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


'''
用Beautiful soup 来拉取网页信息
'''
def soup_analysis(url,headers):
    response=requests.get(url,headers=headers)
    data=response.text
    soup=BeautifulSoup(data,'html.parser')
    print(soup)
    return soup



'''
创建一个execl表格
'''
def create_sheet(title,label_name):
    pic_info=xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet=pic_info.add_sheet(title,cell_overwrite_ok=True)
    sheet.write(0,0,label_name[0])
    sheet.write(0,1,label_name[1])
    return pic_info,sheet



'''
表格更新，记录图片信息
'''
def add_sheet(img_ID,label1,label2,sheet):
    sheet.write(img_ID, 0, label1)
    sheet.write(img_ID, 1, label2)
    img_ID += 1
    return sheet



'''
提取所需要的网页信息，一级一级得到所需要的标题以及图片链接
'''
def extract_info(big_class,big_keyword,small_class,label,soup,sheet,headers,img_ID):
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



'''
主函数
'''
def main(page,sheet_org,img_ID):
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














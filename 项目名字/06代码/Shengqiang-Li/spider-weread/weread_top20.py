#!D:\Anaconda3 python
# -*- coding: UTF-8 -*-

"""
@project: PyCharm
@file: weread_top20.py
@author: Shengqiang Li
@time: 2020/08/08 11:14
@mail: 1312246931@qq.com
"""

from bs4 import BeautifulSoup
from utils import init_logger
import xlwt
import re
import requests
import os

#作者
findauthor = re.compile(r'<p class="wr_bookList_item_author"><a href=(.*?)</a>')
# 书名
findTitle = re.compile(r'<p class="wr_bookList_item_title">(.*)</p>')
#书籍封面
findCover = re.compile(r'<img alt="书籍封面" class="wr_bookCover_img" src="(.*?)"/>')
#简介
findIntro = re.compile(r'<p class="wr_bookList_item_desc">(.*)</p>',re.S)
# 评分
findScore = re.compile(r'<span class="wr_bookList_item_starString">([\d+\.]+)</span>')
#今日阅读人数
findReaderNumber = re.compile(r'<em class="wr_bookList_item_reading_number">([\d+\.]+)</em>')

logger = init_logger(log_file='.\\微信读书.log')

def get_info(url):
    """
    爬取数据
    :param url: 所要爬取的网页的url
    :return: 返回爬取到数据的列表
    """
    datalist = []
    html = requestURL(url)            # 保存网页源码
    logger.info('获取网页源码...')
    soup = BeautifulSoup(html, "html.parser")
    booklist = soup.find('ul',class_="ranking_content_bookList").select('li')
    logger.info('获得书籍列表...')
    for item in booklist:
        data = []
        info = item.find('div',class_="wr_bookList_item_info")
        p = info.find_all('p')
        title = re.findall(findTitle,str(p[0]))[0]
        data.append(title)            #书名
        authors = re.findall(findauthor,str(p[1]))[0]
        author_link,author = authors.split('>')
        data.append(author)           #作者
        intro = re.findall(findIntro,str(p[3]))[0].replace("\n"," ")
        data.append(intro)            #简介
        score = re.findall(findScore,str(p[2]))[0]
        data.append(score)            #评分
        reader = re.findall(findReaderNumber,str(p[2]))[0]
        if float(reader)<100.0:
            reader=float(reader)*10000
        data.append(int(reader))      #今日阅读人数
        cover = item.find('div',class_="wr_bookCover wr_bookList_item_cover")
        img = re.findall(findCover,str(cover))
        data.append(img)              #书籍封面链接
        datalist.append(data)
    return datalist

def requestURL(url):
    """
    获得所要爬取的网页的源码
    :param url: 所要爬取网页的url
    :return:
    """
    try:
        resonse = requests.get(url)
        if resonse.status_code ==200:
            return resonse.text
    except requests.RequestException:
        return None

def saveData(datalist,savepath):
    """
    创建excel表格并将爬取到的数据写入excel
    :param datalist:爬取到的数据的列表
    :param savepath: 保存数据的excel表格的路径
    :return:
    """
    logger.info("开始保存书籍信息...")
    workbook = xlwt.Workbook(encoding="utf-8")           #创建workbook
    worksheet = workbook.add_sheet('微信读书Top20',cell_overwrite_ok=True)
    col = ['书名',"作者名","简介","评分","今日阅读人数","书籍封面"]
    for i in range(0,len(col)):
        worksheet.write(0,i,col[i])
    for i in range(0,len(datalist)):
        logger.info('正在保存第%d本....'%i)
        data = datalist[i]
        for j in range(0,len(col)):
            worksheet.write(i+1,j,data[j])
    workbook.save(savepath)

def download_img(img_url,name):
    '''
    下载图片并保存
    :param img_url: 图片链接地址
    :param name: 图片保存的名字
    :return:图片名
    '''
    try:
        response = requests.get(img_url)
        file_name = name
        if response.status_code ==200:
            open(file_name,'wb').write(response.content)
    except requests.RequestException:
        return 'failed'

def fun_main(url):
    """
    爬取所有榜单的书籍信息并保存
    :param url: type:dict,example:
            url = {'总榜': "https://weread.qq.com/web/category/all",
           '影视原著榜': "https://weread.qq.com/web/category/200000",
           '经典小说榜': "https://weread.qq.com/web/category/600000",
           '文学艺术榜': "https://weread.qq.com/web/category/900000",
           '武侠经典榜': "https://weread.qq.com/web/category/800000",
           }
    """
    for k,v in url.items():
        novel = get_info(v)
        saveData(datalist=novel,savepath='.\\%s.xls'%k)    #保存书籍信息
        for i in range(len(novel)):
            data_single = novel[i]
            download_img(img_url=data_single[5][0],
                         name=os.path.join('.\\pic', '%s_%s.png' % (k,data_single[1])))  #下载书籍封面图片

if __name__ == "__main__":

    url = {'总榜': "https://weread.qq.com/web/category/all",
           '影视原著榜': "https://weread.qq.com/web/category/200000",
           '经典小说榜': "https://weread.qq.com/web/category/600000",
           '文学艺术榜': "https://weread.qq.com/web/category/900000",
           '武侠经典榜': "https://weread.qq.com/web/category/800000",
           }
    fun_main(url=url)







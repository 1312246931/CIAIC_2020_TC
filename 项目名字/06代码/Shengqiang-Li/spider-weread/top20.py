#!D:\Anaconda3 python
# -*- coding: UTF-8 -*-

"""
@project: PyCharm
@file: top20.py
@author: Shengqiang Li
@time: 2020/08/08 11:14
@mail: 1312246931@qq.com
"""

from bs4 import BeautifulSoup
from utils import init_logger
import xlwt
import re
import requests

#bookid
findbookid = re.compile(r'<li maxidx="(\d)" class="wr_bookList_item_link"')
#作者
findauthor = re.compile(r'<p class="wr_bookList_item_author"><a href=(.*?)</a>')
# 书名
findTitle = re.compile(r'<p class="wr_bookList_item_title">(.*)</p>')
#简介
findIntro = re.compile(r'<p class="wr_bookList_item_desc">(.*)</p>',re.S)
# 评分
findScore = re.compile(r'<span class="wr_bookList_item_starString">([\d+\.]+)</span>')
#今日阅读人数
findReaderNumber = re.compile(r'<em class="wr_bookList_item_reading_number">([\d+\.]+)</em>')

logger = init_logger(log_file='.\\微信读书.log')
def main():
    """
    主函数，完成所有功能
    :return:
    """
    url = "https://weread.qq.com/web/category/all"
    datalist = getData(url)
    savepath = ".\\微信读书Top20.xls"
    saveData(datalist,savepath)

def getData(url):
    """
    爬取数据
    :param url: 所要爬取的网页的url
    :return: 返回爬取到数据的列表
    """
    datalist = []
    html = requestURL(url)  # 保存网页源码
    logger.info('Get the source code of the url...')
    soup = BeautifulSoup(html, "html.parser")
    booklist = soup.find('ul',class_="ranking_content_bookList").select('li')
    logger.info('Get the booklist in this page...')
    for item in booklist:
        data = []
        bookid = item.get('bookid')
        data.append(bookid)
        info = item.find('div',class_="wr_bookList_item_info")
        p = info.find_all('p')
        title = re.findall(findTitle,str(p[0]))[0]
        data.append(title)
        authors = re.findall(findauthor,str(p[1]))[0]
        author_link,author = authors.split('>')
        data.append(author)
        intro = re.findall(findIntro,str(p[3]))[0].replace("\n"," ")
        data.append(intro)
        score = re.findall(findScore,str(p[2]))[0]
        data.append(score)
        reader = re.findall(findReaderNumber,str(p[2]))[0]
        if float(reader)<100.0:
            reader=float(reader)*10000
        data.append(int(reader))
        datalist.append(data)
    return datalist

def requestURL(url):
    """
    获得所要爬取的网页的源码
    :param url: 所要爬取网页的url
    :return:
    """
    # head = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
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
    logger.info("Saving...")
    workbook = xlwt.Workbook(encoding="utf-8")           #创建workbook
    worksheet = workbook.add_sheet('微信读数总榜Top20',cell_overwrite_ok=True)
    col = ('bookid','书名',"作者名","简介","评分","今日阅读人数")
    for i in range(0,6):
        worksheet.write(0,i,col[i])
    for i in range(0,20):
        logger.info('Saving the %d....'%i)
        data = datalist[i]
        for j in range(0,6):
            worksheet.write(i+1,j,data[j])
    workbook.save(savepath)

if __name__ == "__main__":
    main()


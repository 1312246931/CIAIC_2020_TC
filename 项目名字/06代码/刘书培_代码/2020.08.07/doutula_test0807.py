
import requests
from bs4 import BeautifulSoup
import xlwt
import os

def request_doutula(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

# list.find(class_='pic-title').find('h1').find('a').string
def save_to_excel(soup):
    #保存为excel
    list = soup.find(class_='list-group-item').find_all(class_='artile_des')
    print(list)
    for item in list:

        item_name = soup.find(class_='list-group-item').find('a').string
        item_time = soup.find(class_='list-group-item').find('span').string
        try:
            item_img = item.find('table').find('img').get('src')
        except AttributeError:
            continue
        print('###############################')
        # print(item_img)
        global n

        sheet.write(n, 0, item_name)
        sheet.write(n, 1, item_time)
        sheet.write(n, 2, item_img)

        n=n+1
    return item_name, item_time


book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('斗图啦套图', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '时间')
sheet.write(0, 2, '图片')

n = 1

src_list = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
url = 'https://www.doutula.com/article/detail/1436139'
#############################
html = request_doutula(url)
soup = BeautifulSoup(html, 'lxml')
##################################
# response = requests.get(url, headers=headers)
# data = response.text
# soup = BeautifulSoup(data, 'html.praser')
# print(soup)
item_name, item_time = save_to_excel(soup)
for i in range(2, 12):
    src = soup.select("div.artile_des:nth-child(" + str(
        i) + ") > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1) > img:nth-child(1)")
    # print(src)
    for src in src:
        src = src.get("src")
        # print('##############################')
        # print(src)
        src_list.append(src)

i=0
for src in src_list:
    i = i+1
    response = requests.get(src, headers=headers)
    data = response.content
    os.getcwd()
    os.makedirs(str(item_name), exist_ok=True)
    file_path="/"+ str(item_name)+ '/' + str(i) +".png"
    with open(os.getcwd() + file_path, "wb") as f:
        f.write(data)
        print("爬取图片+1")

book.save(u'表情包列表.xls')
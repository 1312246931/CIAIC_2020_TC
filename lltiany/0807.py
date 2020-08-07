import json, requests
from lxml import etree


class Wangyiyun(object):
    def __init__(self):
        self.url = 'https://music.163.com/discover/artist'
        self.singer_infos = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        }
        self.parse()

    def get_xpath(self, url):
        response = requests.get(url, headers=self.headers)
        return etree.HTML(response.text)
    # ---------------通过url获取该页面的内容，返回xpath对象

    # --------------通过get_xpath爬取到页面后，我们获取华宇，华宇男等分类
    def parse(self):
        html = self.get_xpath(self.url)
        fenlei_url_list = html.xpath('//ul[@class="nav f-cb"]/li/a/@href')  # 获取华宇等分类的url
        # print(fenlei_url_list)
        # --------将热门和推荐两栏去掉筛选
        new_list = [i for i in fenlei_url_list if 'id' in i]
        for i in new_list:
            fenlei_url = 'https://music.163.com' + i
            self.parse_fenlei(fenlei_url)
            # print(fenlei_url)

    # -------------通过传入的分类url，获取A,B，C页面内容
    def parse_fenlei(self, url):
        html = self.get_xpath(url)
        # 获得字母排序，每个字母的链接
        zimu_url_list = html.xpath('//ul[@id="initial-selector"]/li[position()>1]/a/@href')
        for i in zimu_url_list:
            zimu_url = 'https://music.163.com' + i
            self.parse_singer(zimu_url)

    # ---------------------传入获得的字母链接，开始爬取歌手内容
    def parse_singer(self, url):
        html = self.get_xpath(url)
        item = {}
        singer_names = html.xpath('//ul[@id="m-artist-box"]/li/p/a/text()')
        # --详情页看到页面结构会有两个a标签，所以取第一个
        singer_href = html.xpath('//ul[@id="m-artist-box"]/li/p/a[1]/@href')
        # print(singer_names,singer_href)
        for i, name in enumerate(singer_names):
            item['歌手名'] = name
            item['音乐链接'] = 'https://music.163.com' + singer_href[i].strip()
            # 获取歌手详情页的链接
            url = item['音乐链接'].replace(r'?id', '/desc?id')
            # print(url)
            self.parse_detail(url, item)

            print(item)

    # ---------获取详情页url和存着歌手名字和音乐列表的字典，在字典中添加详情页数据
    def parse_detail(self, url, item):
        html = self.get_xpath(url)
        desc_list = html.xpath('//div[@class="n-artdesc"]/p/text()')[0]
        item['歌手信息'] = desc_list
        self.singer_infos.append(item)
        self.write_singer(item)

    # ----------------将数据字典写入歌手文件
    def write_singer(self, item):
        with open('sing.json', 'a+', encoding='utf-8') as file:
            json.dump(item, file)


music = Wangyiyun()


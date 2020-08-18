from django.shortcuts import render
from bs4 import BeautifulSoup
from .utils import WeatherGet,init_logger
from .utils import fun_query
from .utils import get_info



def fun_weread_classic(request):
	url= {
		  '经典小说榜':"https://weread.qq.com/web/category/600000",
		  }
	classic_novel = get_info(url['经典小说榜'])
	return render(request, 'app001/htmlclassic.html',{'classic_novel':classic_novel})

def fun_weread_total(request):
	url= {'总榜':"https://weread.qq.com/web/category/all",
		  }
	total_noval = get_info(url['总榜'])
	return render(request, 'app001/htmltotal.html',{'total_noval':total_noval})

def fun_weread_la(request):
	url= {
		  '文学艺术榜':"https://weread.qq.com/web/category/900000",
		  }
	la_noval = get_info(url['文学艺术榜'])
	return render(request, 'app001/htmlla.html',{'la_noval':la_noval})

def fun_weread_aa(request):
	url= {
		  '武侠经典榜':"https://weread.qq.com/web/category/800000",
		  }
	aa_noval = get_info(url['武侠经典榜'])
	aa_noval[9][3] = aa_noval[9][3].split('！')[4]
	return render(request, 'app001/htmlaa.html',{'aa_noval':aa_noval})

def fun_weread_ft(request):
	url= {
		  '影视原著榜':"https://weread.qq.com/web/category/200000",
		  }
	ft_noval = get_info(url['影视原著榜'])
	return render(request, 'app001/htmlft.html',{'ft_noval':ft_noval})

def search_form(request):
	return render(request,'app001/htmlsearch.html')

logger=init_logger(log_file='./日志.log')

def search(request):
	#查询天气
	input_content = request.GET['q']                #获得输入的内容
	logger.info('搜索内容为%s'%input_content)
	city_name,city_code = fun_query(p1=input_content)
	logger.info('搜索城市为%s,城市代码为%s'%(city_name,city_code))
	weatherget = WeatherGet(city_code)
	web_info = weatherget.request_weather_web(weatherget.url)  # 抓取网页数据
	soup = BeautifulSoup(web_info, 'html.parser')  # 通过bs4解析网页数据
	weather_info,weather_date,weather_tem_high,weather_tem_low = weatherget.get_weather_info(soup)  # 从网页数据中提取所需数据，并保存
	logger.info('获取到%s的近八日天气信息'%city_name)
	weather_surround=weatherget.get_weather_surroundingregion(soup)
	logger.info('获取到%s周边城市今日的天气信息'%city_name)

	#微信读书
	all_url = "https://weread.qq.com/web/category/all"
	all_novel = get_info(all_url)
	return render(request,'app001/htmldisplay.html',{'wea_info':weather_info,'wea_surround':weather_surround,'city_name':city_name,'all_novel':all_novel,'wea_date':weather_date,'wea_tem_high':weather_tem_high,'wea_tem_low':weather_tem_low})
def fun_method01(request):
	return render(request, 'app001/index.html')

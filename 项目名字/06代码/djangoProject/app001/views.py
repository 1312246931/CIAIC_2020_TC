from django.shortcuts import render
from bs4 import BeautifulSoup
from .weather import WeatherGet,init_logger
from .database_lsq import fun_query
# Create your views here.

def fun_search(request):
	#返回一个页面
	return render(request,'app001/htmlsearch.html')
	pass

logger=init_logger(log_file='./日志.log')

def fun_display(request):
	input_content = request.GET['key01']
	city_name,city_code = fun_query(p1=input_content)
	weatherget = WeatherGet(city_code)
	web_info = weatherget.request_weather_web(weatherget.url)  # 抓取网页数据
	soup = BeautifulSoup(web_info, 'html.parser')  # 通过bs4解析网页数据
	weather_info = weatherget.get_weather_info(soup)  # 从网页数据中提取所需数据，并保存
	weather_surround=weatherget.get_weather_surroundingregion(soup)
	return render(request,'app001/htmldisplay.html',{'wea_info':weather_info,'wea_surround':weather_surround,'city_name':city_name})




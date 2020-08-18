from django.shortcuts import render
from .douban_movie import Douban_Inquire, init_logger
# Create your views here.
def fun_method01(request):
	return render(request,'app003/html04.html')
logger=init_logger(log_file='./日志.log')

def douban(request):
	web_douban = Douban_Inquire()
	infor = web_douban.get_web_douban()
	return render(request, 'app003/html04.html',{'douban_movie_info': infor})
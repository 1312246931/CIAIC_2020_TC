from django.shortcuts import render
import pandas as pd
import numpy as np


# Create your views here.
def fun_method01(request):
	return render(request, 'app004/index.html')

def fun_display01(request):

	info = pd.read_excel('C:\\Users\\Administrator\\Desktop\\django_project_new\\app004\\网易云.xls', sheet_name='网易云')

	link = np.array(info['音乐链接']).tolist()
	singer = np.array(info['歌手名']).tolist()
	intro = np.array(info['歌手信息']).tolist()
	#去掉重复信息
	singer_real = singer[0:4026:10]
	link_real = link[0:4026:10]
	intro_real = intro[0:4026:10]
	#第一个页面所要展示的信息
	singer01 = singer_real[0:80]
	link01 = link_real[0:80]
	intro01 = intro_real[0:80]

	total = []
	for i in range(len(singer01)):
		sig = []
		sig.append(singer01[i])
		sig.append(link01[i])
		sig.append(intro01[i])
		total.append(sig)

	return render(request,'app004/html01.html',{'total':total})

def fun_display02(request):
	info = pd.read_excel('C:\\Users\\Administrator\\Desktop\\django_project_new\\app004\\网易云.xls', sheet_name='网易云')

	link = np.array(info['音乐链接']).tolist()
	singer = np.array(info['歌手名']).tolist()
	intro = np.array(info['歌手信息']).tolist()

	singer_real = singer[0:4026:10]
	link_real = link[0:4026:10]
	intro_real = intro[0:4026:10]

	singer02 = singer_real[80:160]
	link02 = link_real[80:160]
	intro02 = intro_real[80:160]

	total = []
	for i in range(len(singer02)):
		sig = []
		sig.append(singer02[i])
		sig.append(link02[i])
		sig.append(intro02[i])
		total.append(sig)

	return render(request,'app004/html02.html',{'total':total})

def fun_display03(request):

	info = pd.read_excel('C:\\Users\\Administrator\\Desktop\\django_project_new\\app004\\网易云.xls', sheet_name='网易云')

	link = np.array(info['音乐链接']).tolist()
	singer = np.array(info['歌手名']).tolist()
	intro = np.array(info['歌手信息']).tolist()

	singer_real = singer[0:4026:10]
	link_real = link[0:4026:10]
	intro_real = intro[0:4026:10]

	singer03 = singer_real[160:240]
	link03 = link_real[160:240]
	intro03 = intro_real[160:240]

	total = []
	for i in range(len(singer03)):
		sig = []
		sig.append(singer03[i])
		sig.append(link03[i])
		sig.append(intro03[i])
		total.append(sig)
	return render(request,'app004/html03.html',{'total':total})

def fun_display04(request):

	info = pd.read_excel('C:\\Users\\Administrator\\Desktop\\django_project_new\\app004\\网易云.xls', sheet_name='网易云')

	link = np.array(info['音乐链接']).tolist()
	singer = np.array(info['歌手名']).tolist()
	intro = np.array(info['歌手信息']).tolist()

	singer_real = singer[0:4026:10]
	link_real = link[0:4026:10]
	intro_real = intro[0:4026:10]

	singer04 = singer_real[240:320]
	link04 = link_real[240:320]
	intro04 = intro_real[240:320]

	total = []
	for i in range(len(singer04)):
		sig = []
		sig.append(singer04[i])
		sig.append(link04[i])
		sig.append(intro04[i])
		total.append(sig)

	return render(request,'app004/html04.html',{'total':total})

def fun_display05(request):
	info = pd.read_excel('C:\\Users\\Administrator\\Desktop\\django_project_new\\app004\\网易云.xls', sheet_name='网易云')

	link = np.array(info['音乐链接']).tolist()
	singer = np.array(info['歌手名']).tolist()
	intro = np.array(info['歌手信息']).tolist()

	singer_real = singer[0:4026:10]
	link_real = link[0:4026:10]
	intro_real = intro[0:4026:10]

	singer05 = singer_real[320:402]
	link05 = link_real[320:402]
	intro05 = intro_real[320:402]

	total = []
	for i in range(len(singer05)):
		sig = []
		sig.append(singer05[i])
		sig.append(link05[i])
		sig.append(intro05[i])
		total.append(sig)

	return render(request,'app004/html05.html',{'total':total})
from django.shortcuts import render

# Create your views here.
# 显示登陆界面
def fun_view_login(request):
	return render(request,'app002/login.html')

#处理登陆信息
def fun_process_login(request):
	#stage1 获取页面输入的内容
	print(request)
	var_dict=request.GET
	var_user_name=var_dict.get('user_name')
	var_user_password=var_dict.get('user_password')
	#stage2 查询数据库表中是否存在该用户和密码
	if var_user_name=='lsq' and var_user_password=='123456':
		print('登陆成功')
		return render(request,'app002/success.html')
	else:
		print("登陆失败")
		return render(request,'app002/defeat.html')

	#stage3
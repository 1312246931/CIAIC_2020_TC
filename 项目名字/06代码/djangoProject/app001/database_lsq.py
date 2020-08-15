# -*- encoding:utf-8 -*-
'''
	python02_01.py
	======================
	@descript:

	@copyright:chinasoft
	@author:cjgong
	@date:2019-08-02 17:33
'''
import pymysql
import traceback
from tqdm import tqdm
''''
描述：把数据保存到表里
入参：list容器，list容器里的元素是字段里的值

'''
def txt2list(path):
	list_total=[]
	with open(path,'r',encoding='utf-8') as fid:
		for line in fid:
			list_single = []
			num,name = line.strip().split(':')
			list_single.append(str(name))
			list_single.append(str(num))
			list_total.append(list_single)
	return list_total

def fun_insert_method(var_list_data):
	# 步骤1：python代码连接到服务器端
	var_connection = pymysql.connect(host='localhost', port=3306, user='root', password='lsq1101',
									 database='db_01',
									 charset='utf8')
	print('数据库连接对象：', var_connection)

	# 步骤2：把sql语句发送给服务器
	#  创建sql
	var_sql = "insert  into `t_city_infor`(city_name,city_code) values(%s,%s)"
	# 创建游标对象
	var_cursor = var_connection.cursor()
	# 步骤3;服务器端自动执行sql，把执行结果返回
	var_result = var_cursor.execute(var_sql, var_list_data)
	print('mysql服务器端返回的内容：', var_result)
	var_connection.commit()

	# 步骤4：关闭连接
	var_cursor.close()
	var_connection.close()
	pass

#  执行创建表格
def fun_create():
	try:
		var_connection = pymysql.connect(host='localhost', port=3306, user='root', password='lsq1101',
										 database='db_01',
										 charset='utf8')
		print(var_connection)
		# 获取数据库操作对象 游标
		var_cursor = var_connection.cursor()

		var_cursor.execute("DROP TABLE IF EXISTS t_city_infor")
		# 通过游标操作数据库
		var_sql = '''
			CREATE TABLE t_city_infor(
				city_name VARCHAR(20),
				city_code INT(20)
			)
		'''
		var_result = var_cursor.execute(var_sql)
		print('执行结果为：', var_result, '。')
	except Exception as e:
		traceback.print_exc()
	finally:
		# 关闭
		var_cursor.close()
		var_connection.close()
		pass
	pass

# 查询操作
def fun_query(p1):
	try:
		var_connection = pymysql.connect(host='localhost', port=3306, user='root', password='lsq1101',
										 database='db_01',
										 charset='utf8')
		# 获取数据库操作对象 游标
		var_cursor = var_connection.cursor()

		# 通过游标操作数据库
		var_sql = "select city_name,city_code  from t_city_infor where city_name=%s"
		var_cursor.execute(var_sql, (p1,))
		# list容器，list容器里的元素是一个list
		var_result = var_cursor.fetchall()

		return var_result[0][0],var_result[0][1]

	except Exception as e:
		traceback.print_exc()
	finally:
		# 关闭
		var_cursor.close()
		var_connection.close()
		pass
	pass


if __name__ == '__main__':
	# fun_create()
	# #  数据
	var_data = txt2list(path='C:/Users/Administrator/Desktop/python/day06/python06_01/城市代码.txt')
	# total_num=len(var_data)
	# for i in tqdm(range(total_num)):
	# 	fun_insert_method(var_data[i])
	# for element in var_data:
	# 	fun_insert_method(element)
	# 	pass
	fun_query(p1='北京')
	pass

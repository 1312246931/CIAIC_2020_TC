import setuptools

with open("README.MD",'r') as fid:
	long_description = fid.read()

setuptools.setup(name="spider-weread",
				 version="0.0.1",
				 author="Shengqiang-Li",
				 author_email="1312246931@qq.com",
				 description="微信读书爬虫项目",
				 long_description=long_description,
				 long_description_content_type="text/markdown",
				 url="",
				 classifiers=["Programming Language :: Python :: 3","License :: MIT License"],
				 python_requires='>=3.7')
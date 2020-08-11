# 一键导出微信读书个人书架上的书籍和笔记,以及获得微信读书Top20的书籍信息

## 简介

全民阅读的时代已经来临，目前使用读书软件的用户数2.1亿，日活跃用户超过500万，其中19-35岁年轻用户占比超过60%，本科及以上学历用户占比高达80%，北上广深及其他省会城市/直辖市用户占比超过80%。**本人习惯使用微信读书，为了方便整理书籍和导出笔记，便开发了这个小工具。**

## 代码思路

### 1. 目录结构
我们先看一下整体目录结构

```bash
Code
├─ excel_func.py                   读写excel文件
├─ pyqt_gui.py                     PyQt GUI界面
├─wereader.py                     微信读书相关api
├─ top20.py                        获得微信读书榜单Top20的书籍信息
└─ utils.py                        日志函数

```
- excel_func.py
使用xlrd和xlwt库对excel文件进行读写操作

- pyqt_gui.py
使用PyQt绘制GUI界面

- wereader.py
通过抓包解析获得相关api

## 如何运行

```bash
# 跳转到当前目录
cd 目录名
# 先卸载依赖库
pip uninstall -y -r requirement.txt
# 再重新安装依赖库
pip install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# 开始运行
# 获取个人书架上的书籍信息和读数笔记
python pyqt_gui.py
# 获取微信读数榜单上的书籍信息
python top20.py
```

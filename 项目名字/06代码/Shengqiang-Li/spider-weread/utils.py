#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@project: PyCharm
@file: excel_func.py
@author: Shengqiang Li
@time: 2020/08/07 11:14
@mail: 1312246931@qq.com
"""

import logging

def init_logger(log_file=None):
    """
    初始化一个logger
    Ranking of level:CRITICAL(50) == FATAL(50) > ERROR(40) > WARNING(30) == WARN(30) > INFO(20) > DEBUG(10) > NOTSET(0)
    :param log_file: 日志文件的路径
    :return: logger
    """
    log_format = logging.Formatter("[%(asctime)s %(levelname)s] %(message)s")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)                                              #输出级别为INFO级别

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.handlers = [console_handler]

    if log_file and log_file != '':
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)

    return logger
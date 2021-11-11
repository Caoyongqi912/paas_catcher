# -*- coding: utf-8 -*-

# @Time    : 2021/10/20 4:19 下午 
# @Author  : cyq
# @File    : main.py

from mac import Mac

if __name__ == '__main__':
    # 单位秒
    n = 120
    tosee = "同视"
    rzPass = "rzpaas_examp"

    Mac(targetName=tosee ,catch_time=n).catch()

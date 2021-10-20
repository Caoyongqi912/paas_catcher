# -*- coding: utf-8 -*-

# @Time    : 2021/10/20 3:05 下午 
# @Author  : cyq
# @File    : main.py


from iosDevice import IOS


if __name__ == '__main__':
    #单位 秒
    n = 60*60*60
    IOS(n).catch()
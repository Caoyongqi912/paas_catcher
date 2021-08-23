# -*- coding: utf-8 -*-

# @Time    : 2021/8/20 5:56 下午 
# @Author  : cyq
# @File    : opt.py
import enum


class PlaForms(str, enum.Enum):
    IOS = "ios"
    MAC = "mac"
    ANDROID = "android"
    WINDOWS = "windows"

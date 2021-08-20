# -*- coding: utf-8 -*-

# @Time    : 2021/8/12 6:08 下午 
# @Author  : cyq
# @File    : Shell.py

import subprocess


class Shell:

    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        e = errors.decode("utf-8")
        if o:
            return o
        elif e:
            return e



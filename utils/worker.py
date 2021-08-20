# -*- coding: utf-8 -*-

# @Time    : 2021/8/19 5:17 下午 
# @Author  : cyq
# @File    : worker.py
import re
from matplotlib import pyplot


class Worker:

    @staticmethod
    def read(path):
        """
        读取
        :param path: 日志地址
        :return:
        """

        with open(path, "r") as fp:
            body = fp.read()
            cpuInfo = re.findall(r"cpu=(.*?) mem=(.*?)\n", body)
            return cpuInfo

    @staticmethod
    def paint(title: str, avg: str, y_label: str, x_label: str, x: list, y: list, savefig: str):
        """
        绘画
        :param title: 标题
        :param avg: 平均值
        :param y_label: y 标签
        :param x_label: x 标签
        :param x: 数据
        :param y: 数据
        :param savefig: 存放路径
        """
        pyplot.figure(figsize=(20, 10))
        pyplot.title(f"{title} AVG:{avg} MAX:{max(y)} MIN:{min(y)}")
        pyplot.ylabel(y_label)
        pyplot.xlabel(x_label)
        pyplot.plot(x, y)
        pyplot.savefig(savefig)




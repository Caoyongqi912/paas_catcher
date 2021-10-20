# -*- coding: utf-8 -*-

# @Time    : 2021/8/19 5:17 下午 
# @Author  : cyq
# @File    : worker.py
import re
from matplotlib import pyplot

from utils.opt import PlaForms


class Worker:

    @staticmethod
    def read(path, opt: PlaForms):
        """
        读取
        :param path: 日志地址
        :param opt: PlaForms
        :return:
        """
        if opt == PlaForms.MAC:
            with open(path, "r") as fp:
                body = fp.read()
            prefInfo = re.findall(r"rzpaas_example_m(.*?)\n", body)
            _i = []
            for info in prefInfo:
                par = info.strip().split()
                if par[0] != "0.0":
                    _i.append((float(par[0]),par[-3]))
            return _i
        elif opt == PlaForms.IOS:
            with open(path, "r") as fp:
                body = fp.read()
                cpuInfo = re.findall(r"cpu:ts=(.*?);value=(.*?),count=(.*?)\n", body)
                memInfo = re.findall(r"memory:ts=(.*?);value=(.*?)\n", body)
                cpu = []
                mem = []
                for i in cpuInfo:
                    cpu.append((i[0], float(i[1]) / int(i[2])))
                for i in memInfo:
                    mem.append((i[0], float(i[1])))
                print(cpu)
                return cpu, mem

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
        pyplot.xticks(rotation=90)
        pyplot.ylabel(y_label)
        pyplot.xlabel(x_label)
        pyplot.plot(x, y)
        pyplot.savefig(savefig)

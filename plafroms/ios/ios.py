# -*- coding: utf-8 -*-

# @Time    : 2021/8/20 10:03 上午 
# @Author  : cyq
# @File    : ios.py
import time

from ios_device import py_ios_device


class Ios:

    def __init__(self):
        self.name = "rzpaas_example_ios"
        self.ios = py_ios_device.PyiOSDevice()

    def getChannel(self):
        """
         获取当前设备有哪些服务
        :return: list
        """
        return self.ios.get_channel()

    def getNetwork(self):
        self.ios.start_get_network(Ios.callBack)
        time.sleep(10)
        self.ios.stop_get_network()

    def getApps(self):
        return self.ios.get_applications()

    def getProcess(self):
        return self.ios.get_processes()

    def getCPU(self):
        self.ios.start_get_gpu(Ios.callBack)

    @staticmethod
    def callBack(res):
        print(res)


if __name__ == '__main__':
    ios = Ios()
    ios.getCPU()
    ios.getNetwork()
    # for i in ios.getProcess():
    #     print(i)

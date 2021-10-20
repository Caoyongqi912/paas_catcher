# -*- coding: utf-8 -*-

# @Time    : 2021/8/20 10:03 上午 
# @Author  : cyq
# @File    : ios.py
import json
import time

from ios_device import py_ios_device
import tidevice

from utils.Shell import Shell


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
    ios.getNetwork()
    print(ios.getApps())
    # # ios.getNetwork()
    # for i in ios.getProcess():
    #     print(i)
    # "pyidevice instruments sysmontap -p 379  --proc_filter memVirtualSize,cpuUsage --processes"
    # "379 rzpaas_example_ios       com.duobei.rzpaas-example-ios PaaSTest"
    # cmd = "tidevice perf -B com.duobei.rzpaas-example-ios >> ios_out.txt"
    # Shell.invoke(cmd)

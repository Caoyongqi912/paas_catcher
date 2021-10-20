# -*- coding: utf-8 -*-

# @Time    : 2021/8/20 2:59 下午 
# @Author  : cyq
# @File    : iosDevice.py
import os
import time

import tidevice
from tidevice import DataType
from utils.worker import Worker
from utils.opt import PlaForms


class IOS:
    t = tidevice.Device()
    perf = tidevice.Performance(t, [DataType.CPU, DataType.MEMORY])
    path = os.path.join(os.path.dirname(__file__), "ios_out.txt")

    def __init__(self, catch_time: int = 0):
        self.ctime = catch_time

        if os.path.exists(self.path):
            os.remove(self.path)

    def catch(self):

        self._start()
        cpu = []
        cpuNum = []
        mem = []
        memNum = []

        cpuInfo, memInfo = Worker.read(self.path, PlaForms.IOS)
        for c in cpuInfo:
            cpu.append(round(c[1], 2))
            t = time.strftime("%H:%M:%S", time.localtime(int(c[0])))
            cpuNum.append(t)
        for m in memInfo:
            mem.append(round(m[1], 2))
            t = time.strftime("%H:%M:%S", time.localtime(int(m[0])))
            memNum.append(t)

        cpuPic = os.path.join(os.path.dirname(__file__), "ios_cpu.jpg")
        memPic = os.path.join(os.path.dirname(__file__), "ios_mem.jpg")

        cpu_avg = f"{round(sum(cpu) / len(cpu), 2)}%"
        mem_avg = f"{round(sum(mem) / len(mem), 2)}M"

        Worker.paint(title="IOS_CPU", avg=cpu_avg, y_label="CPU(%)", x_label="Time", x=cpuNum, y=cpu, savefig=cpuPic)
        Worker.paint(title="IOS_MEM", avg=mem_avg, y_label="Mem(M)", x_label="Time", x=memNum, y=mem, savefig=memPic)

    def _start(self):
        print("请确认开启paas test")

        self.perf.start("com.duobei.rzpaas-example-ios", IOS.callback)
        time.sleep(self.ctime)
        self.perf.stop()
        print("结束")
        return

    @staticmethod
    def callback(_type: DataType, value: dict):
        now = time.strftime("%H:%M:%S", time.localtime(value["timestamp"]))
        print(f"run.. time = {now}")

        with open(IOS.path, "a") as fp:
            if _type.value == "cpu":
                fp.write(_type.value + f":ts={value['timestamp']};value={value['value']},count={value['count']}\n")
            else:
                fp.write(_type.value + f":ts={value['timestamp']};value={value['value']}\n")


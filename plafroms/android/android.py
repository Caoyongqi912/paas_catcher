# -*- coding: utf-8 -*-

# @Time    : 2021/8/23 2:48 下午 
# @Author  : cyq
# @File    : android.py
import os
from plafroms.android.DeviceInfo import DeviceInfo
from utils.worker import Worker


class ANDROID:
    device = DeviceInfo()
    path = os.path.join(os.path.dirname(__file__), "and_out.txt")

    def __init__(self, catch_time: int = 0):
        self.cpuList = []
        self.memList = []

        self.ctime = catch_time
        self.id = self.device.get_device_id()
        self.kel = self.device.get_cpu_kel(self.id)
        self.pla = self.device.get_current_package_name(self.id)[0]

        if os.path.exists(self.path):
            os.remove(self.path)

    def catch(self):
        print("start")
        for t in range(self.ctime):
            print(f"catch step {t} ..")
            self._start()
        print("over")
        cpuPic = os.path.join(os.path.dirname(__file__), "android_cpu.jpg")
        memPic = os.path.join(os.path.dirname(__file__), "android_mem.jpg")

        cpuNum = [i for i in range(len(self.cpuList))]
        memNum = [i for i in range(len(self.memList))]

        cpu_avg = round(sum(self.cpuList) / len(self.cpuList), 2)
        mem_avg = round(sum(self.memList) / len(self.memList), 2)

        Worker.paint(title="MAC_CPU", avg=cpu_avg, y_label="CPU(%)", x_label="Time", x=cpuNum, y=self.cpuList,
                     savefig=cpuPic)
        Worker.paint(title="MAC_MEM", avg=mem_avg, y_label="Mem(M)", x_label="Time", x=memNum, y=self.memList,
                     savefig=memPic)

    def _start(self):

        cpu = self.device.get_cup_info(self.id, self.pla) / self.kel
        mem = self.device.get_memory_info(self.id, self.pla)
        self.cpuList.append(cpu)
        self.memList.append(mem)
        with open(self.path, "a") as fp:
            fp.write(f"cpu={cpu};mem={mem}\n")
        return

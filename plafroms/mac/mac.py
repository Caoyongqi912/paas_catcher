# -*- coding: utf-8 -*-

# @Time    : 2021/8/19 5:21 下午 
# @Author  : cyq
# @File    : mac.py
import os

from utils.Shell import Shell
from utils.opt import PlaForms
from utils.worker import Worker


class Mac:

    def __init__(self, targetName: str, catch_time: int = 0):
        """
        init
        :param catch_time: 测试时间 xh
        """
        self.targetName = targetName
        if self.targetName == "同视":
            self.targetName  += "   "
        self.ctime = catch_time

    def catch(self):
        path = os.path.join(os.path.dirname(__file__), "mac_out.txt")
        if os.path.exists(path):
            os.remove(path)

        _cmd = f"top  -l 10 -s 1 -ncols 10 | grep -E '{self.targetName}' >>" + path
        print(f"测试开始。 请确认已开启 {self.targetName}")
        for t in range(int(self.ctime / 10)):
            Shell.invoke(_cmd)
            print(f"catch step {t} ..")
        print("测试结束，生成测试报告中。。。。")
        print(path)
        info = Worker.read(path, opt=PlaForms.MAC,target=self.targetName.strip())
        cpu = []
        mem = []
        print(info)
        for i in info:
            if self.targetName != "rzpaas_examp":
                cpu.append(float(i[0]))
            else:
                cpu.append(float(i[0]) / 8)
            mem.append(float(i[1].split("M")[0]))

        cpuNum = [i for i in range(len(cpu))]
        cpuPic = os.path.join(os.path.dirname(__file__), f"mac_cpu_{self.targetName.strip()}.jpg")
        memNum = [i for i in range(len(mem))]
        memPic = os.path.join(os.path.dirname(__file__), f"mac_mem_{self.targetName.strip()}.jpg")

        cpu_avg = f"{round(sum(cpu) / len(cpu), 2)}%"
        mem_avg = f"{round(sum(mem) / len(mem), 2)}M"

        Worker.paint(title="MAC_CPU", avg=cpu_avg, y_label="CPU(%)", x_label="Time", x=cpuNum, y=cpu, savefig=cpuPic)
        Worker.paint(title="MAC_MEM", avg=mem_avg, y_label="Mem(M)", x_label="Time", x=memNum, y=mem, savefig=memPic)

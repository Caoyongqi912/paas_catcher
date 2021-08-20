from plafroms.ios.iosDevice import IOS
from plafroms.mac.mac import Mac


def run(plat, s):
    if plat == "mac":
        Mac(s).catch()
    elif plat == "win":
        pass
    elif plat == "and":
        pass
    elif plat == "ios":
        IOS(s).catch()
    else:
        print("?")


if __name__ == '__main__':
    """
    mac 1 = 1h *10
    
    ios 1 = 1h
    """
    run("mac", 1)

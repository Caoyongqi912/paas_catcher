from plafroms.mac.mac import Mac


def run(plat, s):
    if plat == "mac":
        Mac(s).catch()
    elif plat == "win":
        pass
    elif plat == "and":
        pass
    elif plat == "ios":
        pass
    else:
        print("?")


if __name__ == '__main__':
    run("mac", 1)

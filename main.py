from plafroms.android.android import ANDROID
from plafroms.ios.iosDevice import IOS
from plafroms.mac.mac import Mac
from utils.opt import PlaForms


def run(plat: str, t):
    if plat == PlaForms.MAC:
        Mac(t).catch()
    elif plat == PlaForms.ANDROID:
        ANDROID(t).catch()
    elif plat == PlaForms.IOS:
        IOS(t).catch()
    elif plat == PlaForms.WINDOWS:
        print("==")
    else:
        print("?")


if __name__ == '__main__':
    """
    mac 1 = 1h
    ios 1 = 1h
    android 1 = 1h
    """
    run("android", 0.2)

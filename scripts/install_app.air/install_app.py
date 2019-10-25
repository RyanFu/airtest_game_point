# -*- encoding=utf8 -*-

__author__ = "tianyabin"
__title__ = '安装APP'
__desc__ = '''1安装apk
            2、启动app，并等待启动界面'''

from airtest.core.api import *
from utils import *
auto_setup(__file__)


def install_DHM():
    time_tup = time.localtime(time.time())
    format_time = '%Y-%m-%d_%a_%H-%M-%S'
    apksName = time.strftime(format_time, time_tup)
    build_device_apks = 'D:\\testdir\\Result\\DHM_Release\\' + apksName + '.apks'
    # 通过AAB构建APKS----代替---install(apk_path)
    Build = os.system(
        'java -jar D:\\testdir\\lib\\bundletool-all-0.10.2.jar build-apks --connected-device --bundle=D:\\testdir\\Result\\DHM_Release\\DHM_Release.aab --output=' + build_device_apks + ' --ks=D:\\testdir\\lib\\signature.keystore --ks-pass=pass:123456 --ks-key-alias=key --key-pass=pass:123456')
    if Build == 0:
        log('DHM构建成功')
        Install = os.system(
            'java -jar D:\\testdir\\lib\\bundletool-all-0.10.2.jar install-apks --apks=' + build_device_apks)
        # 构建成功安装APKS
        if Install == 0:
            log('DHM安装成功')
            Logging('DHM安装成功')
            sleep(2)
        else:
            log('DHM安装失败')
            Logging('DHM安装失败')
            pass
    else:
        log('DHM构建失败')
        Logging('DHM构建失败')

def install_IWS():
    time_tup = time.localtime(time.time())
    format_time = '%Y-%m-%d_%a_%H-%M-%S'
    apksName = time.strftime(format_time, time_tup)
    build_device_apks = 'D:\\testdir\\Result\\IWS_Release\\' + apksName + '.apks'
    # 通过AAB构建APKS----代替---install(apk_path)
    Build = os.system(
        'java -jar D:\\testdir\\lib\\bundletool-all-0.10.2.jar build-apks --connected-device --bundle=D:\\testdir\\Result\\IWS_Release\\IdleWizardSchool.aab --output=' + build_device_apks + ' --ks=D:\\testdir\\lib\\signature.keystore --ks-pass=pass:123456 --ks-key-alias=key --key-pass=pass:123456')
    if Build == 0:
        log('IWS构建成功')
        Install = os.system(
            'java -jar D:\\testdir\\lib\\bundletool-all-0.10.2.jar install-apks --apks=' + build_device_apks)
        # 构建成功安装APKS
        if Install == 0:
            log('IWS安装成功')
            Logging('IWS安装成功')
            sleep(2)
        else:
            log('IWS安装失败')
            Logging('IWS安装失败')
            pass
    else:
        log('IWS构建失败')
        Logging('IWS构建失败')
def install_TBC():
    app_id = "com.toybrickcrush.casual.avidly"
    app_path ="D:\\testdir\\Result\\ToyBrickCrush.apk"
    Install = os.system(
        'adb install ' + app_path)
    # 构建成功安装APKS
    if Install == 0:
        log('TBC安装成功')
        Logging('TBC安装成功')
        sleep(2)

    else:
        log('TBC安装失败')
        Logging('TBC安装失败')
        pass


def install_BP():
    app_path = "D:\\testdir\\Result\\bingoparty.apk"
    Install = os.system(
        'adb install ' + app_path)
    # 构建成功安装APKS
    if Install == 0:
        log('BP安装成功')
        Logging('BP安装成功')
        sleep(2)

    else:
        log('BP安装失败')
        Logging('BP安装失败')
        pass

def install_BJ():
    app_path = "D:\\testdir\\Result\\bingojourney.apk"
    install = os.system(
        'adb install ' + app_path)
    # 构建成功安装APKS
    if install == 0:
        log('BJ安装成功')
        Logging('BJ安装成功')
        sleep(2)

    else:
        log('BJ安装失败')
        Logging('BJ安装失败')
        pass

def install_BB():
    app_path = "D:\\testdir\\Result\\bingoblaze.apk"
    Install = os.system(
        'adb install ' + app_path)
    # 构建成功安装APKS
    if Install == 0:
        log('BB安装成功')
        Logging('BB安装成功')
        sleep(2)

    else:
        log('BB安装失败')
        Logging('BB安装失败')
        pass
def install_DW():
    app_path = "D:\\testdir\\Result\\DoubleWin.apk"
    Install = os.system(
        'adb install ' + app_path)
    # 构建成功安装APKS
    if Install == 0:
        log('DW安装成功')
        Logging('DW安装成功')
        sleep(2)

    else:
        log('DW安装失败')
        Logging('DW安装失败')
        pass

#安装DHM
try:
    install_DHM()
except:
    log('DHM安装失败')
    Logging('DHM安装失败')
    pass
#安装Binggoparty
try:
    install_BP()
except:
    log('BP安装失败')
    Logging('BP安装失败')
    pass
#安装Binggoblaze
try:
    install_BB()
except:
    log('BB安装失败')
    Logging('BB安装失败')
    pass
#安装Binggojourny
try:
    install_BJ()
except:
    log('BJ安装失败')
    Logging('BJ安装失败')
    pass
#安装doubolewin
try:
    install_DW()
except:
    log('DW安装失败')
    Logging('DW安装失败')
    pass

try:
    install_IWS()
except:
    log('IWS安装失败')
    Logging('IWS安装失败')
    pass
# try:
#     install_TBC()
# except:
#     log('TBC安装失败')
#     Logging('TBC安装失败')
#     pass



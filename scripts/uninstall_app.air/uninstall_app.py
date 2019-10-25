# -*- encoding=utf8 -*-

__author__ = "tianyabin"
__title__ = '卸载安装APP'
__desc__ = '''1、卸载apk
            2、启动app，并等待启动界面'''

from airtest.core.api import *

from utils import *
auto_setup(__file__)
def uninstall_DHM():
    status = os.popen(
        'adb uninstall com.dreamhomematch.casual.free')
    list = status.readlines()
    if list[0].find('Success') >= 0:
        log('DHM卸载执行成功---')
        Logging('DHM卸载执行成功---')
    elif list[0].find('Failure') >= 0:
        log('DHM卸载失败---')
        Logging('DHM卸载失败---')
    else:
        log('DHM命令异常---')
        Logging('DHM命令异常---')

def uninstall_TBC():
    status = os.popen(
        'adb uninstall com.toybrickcrush.casual.avidly')
    list = status.readlines()
    if list[0].find('Success') >= 0:
        log('TBC卸载执行成功---')
        Logging('TBC卸载执行成功---')
    elif list[0].find('Failure') >= 0:
        log('TBC卸载失败---')
        Logging('TBC卸载失败---')
    else:
        log('TBC命令异常---')
        Logging('TBC\命令异常---')
#binggoblaze
def uninstall_BB():
    status = os.popen(
        'adb uninstall com.bingo.blaze.free')
    list = status.readlines()
    if list[0].find('Success') >= 0:
        log('BB卸载执行成功---')
        Logging('BB卸载执行成功---')
    elif list[0].find('Failure') >= 0:
        log('BB卸载失败---')
        Logging('BB卸载失败---')
    else:
        log('BB命令异常---')
        Logging('BB命令异常---')
#binggoparty
def uninstall_BP():
    status = os.popen(
        'adb uninstall com.bingo.tour.party.crazy.free')
    list = status.readlines()
    if list[0].find('Success') >= 0:
        log('BP卸载执行成功---')
        Logging('BP卸载执行成功---')
    elif list[0].find('Failure') >= 0:
        log('BP卸载失败---')
        Logging('BP卸载失败---')
    else:
        log('BP命令异常---')
        Logging('BP命令异常---')

#binggojourny
def uninstall_BJ():
    status = os.popen(
        'adb uninstall com.bingo.scape.android.free')
    list = status.readlines()
    if list[0].find('Success') >= 0:
        log('BJ卸载执行成功---')
        Logging('BJ卸载执行成功---')
    elif list[0].find('Failure') >= 0:
        log('BJ卸载失败---')
        Logging('BJ卸载失败---')
    else:
        log('BJ命令异常---')
        Logging('BJ命令异常---')
#DoubleWin
def uninstall_DW():
    status = os.popen(
        'adb uninstall com.huge.slots.casino.vegas.amazon.avidly')
    list = status.readlines()
    if list[0].find('Success') >= 0:
        log('DW卸载执行成功---')
        Logging('DW卸载执行成功---')
    elif list[0].find('Failure') >= 0:
        log('DW卸载失败---')
        Logging('DW卸载失败---')
    else:
        log('DW命令异常---')
        Logging('DW命令异常---')

#IWS
def uninstall_IWS():
    status = os.popen(
        'adb uninstall p.jerryzhang.idlewizardschool')
    list = status.readlines()
    if list[0].find('Success') >= 0:
        log('IWS卸载执行成功---')
        Logging('IWS卸载执行成功---')
    elif list[0].find('Failure') >= 0:
        log('IWS卸载失败---')
        Logging('IWS卸载失败---')
    else:
        log('IWS命令异常---')
        Logging('IWS命令异常---')



try:
    uninstall_DHM()
except:
    Logging('DHM命令异常---')
    pass

try:
    uninstall_BP()
except:
    Logging('BP命令异常---')
    pass

try:
    uninstall_BB()
except:
    Logging('BB命令异常---')
    pass

try:
    uninstall_BJ()
except:
    Logging('BJ命令异常---')
    pass

try:
    uninstall_DW()
except:
    Logging('DW命令异常---')
    pass

try:
    uninstall_IWS()
except:
    Logging('IWS命令异常---')
    pass
# try:
#     uninstall_TBC()
# except:
#     Logging('TBC命令异常---')
#     pass
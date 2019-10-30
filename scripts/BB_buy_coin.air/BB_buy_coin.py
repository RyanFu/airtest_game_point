# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *
from constant import *
auto_setup(__file__)
app_id='com.bingo.blaze.free'
time=5
start_app(app_id)
sleep(20)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco.click([0.72,0.73])
sleep(5)
if poco("com.android.packageinstaller:id/permission_allow_button").exists():
    poco("com.android.packageinstaller:id/permission_allow_button").click()
sleep(5)
if login_mode=='local':
    if exists(Template(r"tpl1572246984758.png", record_pos=(0.243, 0.104), resolution=(2560, 1440))):
        poco.click([0.74,0.86])
        sleep(10)
else:
    if exists(Template(r"tpl1572246984758.png", record_pos=(0.243, 0.104), resolution=(2560, 1440))):
        touch(Template(r"tpl1572246984758.png", record_pos=(0.243, 0.104), resolution=(2560, 1440)))
        sleep(20)

while True:

    if exists(Template(r"tpl1572247109054.png", record_pos=(0.382, -0.219), resolution=(2560, 1440))):
        touch(Template(r"tpl1572247109054.png", record_pos=(0.382, -0.219), resolution=(2560, 1440)))
        sleep(3)
    if exists(Template(r"tpl1572247799939.png", record_pos=(0.423, -0.231), resolution=(2560, 1440))):
        touch(Template(r"tpl1572247799939.png", record_pos=(0.423, -0.231), resolution=(2560, 1440)))
        sleep(5)

    if exists(Template(r"tpl1572247156267.png", record_pos=(-0.03, -0.241), resolution=(2560, 1440))):
        break
#进入首页
if exists(Template(r"tpl1572247156267.png", record_pos=(-0.03, -0.241), resolution=(2560, 1440))):
    poco.click([0.46,0.07])
    sleep(5)
    if exists(Template(r"tpl1572247250063.png", record_pos=(0.333, -0.135), resolution=(2560, 1440))):
        touch(Template(r"tpl1572247250063.png", record_pos=(0.333, -0.135), resolution=(2560, 1440)))
        sleep(15)
        poco.click([0.5,0.9])
        sleep(20)
        i=5
        while True:            
            i-=1
            if i==1:
                keyevent("BACK")
                break
            if exists(Template(r"tpl1572247334620.png", record_pos=(0.321, 0.214), resolution=(2560, 1440))):
                touch(Template(r"tpl1572247334620.png", record_pos=(0.321, 0.214), resolution=(2560, 1440)))
                sleep(5)
            if exists(Template(r"tpl1572247370344.png", record_pos=(-0.003, 0.198), resolution=(2560, 1440))):
                touch(Template(r"tpl1572247370344.png", record_pos=(-0.003, 0.198), resolution=(2560, 1440)))
                sleep(5)
            if exists(Template(r"tpl1572247109054.png", record_pos=(0.382, -0.219), resolution=(2560, 1440))):
                touch(Template(r"tpl1572247109054.png", record_pos=(0.382, -0.219), resolution=(2560, 1440)))
                sleep(3)
            if exists(Template(r"tpl1572247156267.png", record_pos=(-0.03, -0.241), resolution=(2560, 1440))):
                break

stop_app(app_id)


    








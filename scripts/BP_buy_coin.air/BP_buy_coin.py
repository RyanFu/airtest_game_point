# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *
from constant import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

app_id = 'com.bingo.tour.party.crazy.free'
start_app(app_id)
sleep(20)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco.click([0.72,0.73])
sleep(5)
if poco("com.android.packageinstaller:id/permission_allow_button").exists():
    poco("com.android.packageinstaller:id/permission_allow_button").click()
sleep(5)
#登录
if login_mode=='local':
    if exists(Template(r"tpl1572229515467.png", record_pos=(0.247, 0.185), resolution=(2160, 1080))):
        touch(Template(r"tpl1572229515467.png", record_pos=(0.247, 0.185), resolution=(2160, 1080)))
        sleep(10)
else:
    if exists(Template(r"tpl1572229536170.png", record_pos=(-0.0, 0.172), resolution=(2160, 1080))):
        touch(Template(r"tpl1572229536170.png", record_pos=(-0.0, 0.172), resolution=(2160, 1080)))
        sleep(30)
sleep(5)    
while True:
    if exists(Template(r"tpl1572229675665.png", record_pos=(0.341, -0.194), resolution=(2160, 1080))):
        touch(Template(r"tpl1572229675665.png", record_pos=(0.341, -0.194), resolution=(2160, 1080)))
        sleep(3)
    else:
        if exists(Template(r"tpl1572229786058.png", record_pos=(-0.022, -0.213), resolution=(2160, 1080))):
            break
        
sleep(5)  
#购买支付
if exists(Template(r"tpl1572229786058.png", record_pos=(-0.022, -0.213), resolution=(2160, 1080))):
    #touch(Template(r"tpl1572229786058.png", record_pos=(-0.022, -0.213), resolution=(2160, 1080)))
    poco.click([0.47,0.06])
    sleep(5)
    if exists(Template(r"tpl1572229881225.png", record_pos=(0.298, -0.116), resolution=(2160, 1080))):
        touch(Template(r"tpl1572229881225.png", record_pos=(0.298, -0.116), resolution=(2160, 1080)))
        sleep(15)
        poco.click([0.5,0.9])
        sleep(20)
        i=5
        while True:
            i -= 1
            if i == 1:
                keyevent("BACK")
                break
            if exists(Template(r"tpl1572242375291.png", record_pos=(0.32, 0.21), resolution=(1920, 1080))):
                touch(Template(r"tpl1572242375291.png", record_pos=(0.32, 0.21), resolution=(1920, 1080)))
                sleep(10)
            if exists(Template(r"tpl1572242422086.png", record_pos=(0.003, 0.195), resolution=(1920, 1080))):
                touch(Template(r"tpl1572242422086.png", record_pos=(0.003, 0.195), resolution=(1920, 1080)))
                sleep(10)
            if exists(Template(r"tpl1572229675665.png", record_pos=(0.341, -0.194), resolution=(2160, 1080))):
                touch(Template(r"tpl1572229675665.png", record_pos=(0.341, -0.194), resolution=(2160, 1080)))
                sleep(3)
stop_app(app_id)


            
    

    

       












    

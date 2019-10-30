# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *
from constant import *


auto_setup(__file__)
app_id='com.huge.slots.casino.vegas.android.avidly'
start_app(app_id)
sleep(20)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
if exists(Template(r"tpl1572321674058.png", record_pos=(0.006, 0.219), resolution=(2560, 1440))):
    touch(Template(r"tpl1572321674058.png", record_pos=(0.006, 0.219), resolution=(2560, 1440)))
    sleep(3)
if login_mode=='local':
    if exists(Template(r"tpl1572321720658.png", record_pos=(0.018, 0.203), resolution=(2560, 1440))):
        poco.click([0.73,0.85])
        sleep(30)
else:
    if exists(Template(r"tpl1572321720658.png", record_pos=(0.018, 0.203), resolution=(2560, 1440))):
        touch(Template(r"tpl1572321720658.png", record_pos=(0.018, 0.203), resolution=(2560, 1440)))
        sleep(30)
if exists(Template(r"tpl1572321920350.png", record_pos=(-0.004, 0.166), resolution=(2560, 1440))):
    touch(Template(r"tpl1572321920350.png", record_pos=(-0.004, 0.166), resolution=(2560, 1440)))
    sleep(5)
i = 5
while True:
    i-=1
    if i==1:
        break
    if exists(Template(r"tpl1572322048064.png", record_pos=(0.432, -0.202), resolution=(2560, 1440))):
        
        touch(Template(r"tpl1572322048064.png", record_pos=(0.432, -0.202), resolution=(2560, 1440)))
        sleep(3)
    if exists(Template(r"tpl1572322088412.png", record_pos=(0.317, -0.192), resolution=(2560, 1440))):
        touch(Template(r"tpl1572322088412.png", record_pos=(0.317, -0.192), resolution=(2560, 1440)))
        sleep(3)
    if exists(Template(r"tpl1572322407065.png", record_pos=(0.456, -0.243), resolution=(2560, 1440))):
        touch(Template(r"tpl1572322407065.png", record_pos=(0.456, -0.243), resolution=(2560, 1440)))
        sleep(3)
        
    if exists(Template(r"tpl1572322488196.png", record_pos=(0.425, -0.218), resolution=(2560, 1440))):
        touch(Template(r"tpl1572322488196.png", record_pos=(0.425, -0.218), resolution=(2560, 1440)))
        sleep(3)
    if exists(Template(r"tpl1572322560813.png", record_pos=(0.43, -0.231), resolution=(2560, 1440))):
        touch(Template(r"tpl1572322560813.png", record_pos=(0.43, -0.231), resolution=(2560, 1440)))
        sleep(3)
    poco.click([0.04,0.16])
    
    if exists(Template(r"tpl1572322763182.png", record_pos=(0.003, -0.247), resolution=(2560, 1440))):
        break

if exists(Template(r"tpl1572322763182.png", record_pos=(0.003, -0.247), resolution=(2560, 1440))):#进入购买
    touch(Template(r"tpl1572322763182.png", record_pos=(0.003, -0.247), resolution=(2560, 1440)))
    sleep(5)
    if exists(Template(r"tpl1572322899475.png", record_pos=(0.318, -0.132), resolution=(2560, 1440))):
        touch(Template(r"tpl1572322899475.png", record_pos=(0.318, -0.132), resolution=(2560, 1440)))
        sleep(15)
        if poco('一键购买').exists():
            poco('一键购买').click()
            sleep(15)
            if exists(Template(r"tpl1572323059575.png", record_pos=(0.004, 0.192), resolution=(2560, 1440))):
                touch(Template(r"tpl1572323059575.png", record_pos=(0.004, 0.192), resolution=(2560, 1440)))
                sleep(3)
            if exists(Template(r"tpl1572323105855.png", record_pos=(0.398, -0.193), resolution=(2560, 1440))):
                touch(Template(r"tpl1572323105855.png", record_pos=(0.398, -0.193), resolution=(2560, 1440)))
                sleep(3)
            if exists(Template(r"tpl1572323151167.png", record_pos=(0.433, -0.226), resolution=(2560, 1440))):
                touch(Template(r"tpl1572323151167.png", record_pos=(0.433, -0.226), resolution=(2560, 1440)))
                sleep(3)
stop_app(app_id)




        






    




# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *

from constant import *
auto_setup(__file__)
app_id='com.bingo.scape.android.free'
start_app(app_id)
sleep(20)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

if login_mode=='local':
    if exists(Template(r"tpl1572315207964.png", record_pos=(0.002, 0.193), resolution=(2560, 1440))):
        poco.click([0.71,0.82])
        sleep(10)
else:
    if exists(Template(r"tpl1572315207964.png", record_pos=(0.002, 0.193), resolution=(2560, 1440))):
        touch(Template(r"tpl1572315207964.png", record_pos=(0.002, 0.193), resolution=(2560, 1440)))
        sleep(20)
if exists(Template(r"tpl1572315420911.png", record_pos=(0.003, 0.171), resolution=(2560, 1440))):
    touch(Template(r"tpl1572315420911.png", record_pos=(0.003, 0.171), resolution=(2560, 1440)))
    sleep(5)
if exists(Template(r"tpl1572315490218.png", record_pos=(-0.105, -0.213), resolution=(2560, 1440))):
    pass
i =5
while True:
    i-=i
    if i==1:
        break
    if exists(Template(r"tpl1572315875251.png", record_pos=(0.463, -0.247), resolution=(2560, 1440))):
        touch(Template(r"tpl1572315875251.png", record_pos=(0.463, -0.247), resolution=(2560, 1440)))
        sleep(3)
    if exists(Template(r"tpl1572316227821.png", record_pos=(0.314, -0.172), resolution=(2560, 1440))):
        touch(Template(r"tpl1572316227821.png", record_pos=(0.314, -0.172), resolution=(2560, 1440)))
        sleep(3)
    if exists(Template(r"tpl1572316650111.png", record_pos=(-0.344, -0.186), resolution=(2560, 1440))):
        break
if exists(Template(r"tpl1572316650111.png", record_pos=(-0.344, -0.186), resolution=(2560, 1440))):#进入首页
    poco.click([0.148,0.16])
    sleep(5)
    if exists(Template(r"tpl1572316875864.png", record_pos=(-0.111, 0.159), resolution=(2560, 1440))):
        touch(Template(r"tpl1572316875864.png", record_pos=(-0.111, 0.159), resolution=(2560, 1440)))
        sleep(15)
    elif exists(Template(r"tpl1572316933491.png", record_pos=(0.122, 0.158), resolution=(2560, 1440))):
        touch(Template(r"tpl1572316933491.png", record_pos=(0.122, 0.158), resolution=(2560, 1440)))
        sleep(15)
    else:
        pass
    if poco('一键购买').exists():
        poco('一键购买').click()
        sleep(20)

stop_app(app_id)    


        
    






    

          
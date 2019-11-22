# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *

auto_setup(__file__)
wake()
sleep(3)

touch(Template(r"tpl1573696774549.png", record_pos=(-0.276, 0.228), resolution=(1440, 2560)))
touch(Template(r"tpl1573696788065.png", record_pos=(-0.002, 0.225), resolution=(1440, 2560)))
touch(Template(r"tpl1573696794437.png", record_pos=(0.293, 0.225), resolution=(1440, 2560)))
touch(Template(r"tpl1573696806296.png", record_pos=(-0.277, 0.351), resolution=(1440, 2560)))
touch(Template(r"tpl1573696815277.png", record_pos=(0.28, 0.669), resolution=(1440, 2560)))

start_app('com.alibaba.android.rimet')
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
sleep(3)
poco(text="狂热网络").click()
sleep(5)
touch(Template(r"tpl1571217025096.png", record_pos=(-0.343, 0.069), resolution=(1080, 2160)))
sleep(10)
poco("更新打卡").click()
sleep(5)
poco(text="确定").click()
sleep(5)
poco("我知道了").click()
sleep(5)
stop_app('com.alibaba.android.rimet')

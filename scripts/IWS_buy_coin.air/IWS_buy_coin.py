# -*- encoding=utf8 -*-
__author__ = "chihai"
# from utils import *
from airtest.core.api import *
auto_setup(__file__)
app_id= 'p.jerryzhang.idlewizardschool'
from utils import *
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


start_app('com.android.chrome')
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

sleep(5)
poco("com.android.chrome:id/home_button").click()
sleep(5)
poco("com.android.chrome:id/search_box_text").click()
text('https://play.google.com/apps/test/RQ940hvJP70/ahAAvZMmj3zTQ2NC7auqjhxaiJOOV5ZISLbjGWIKqmj8AAC3-mbZt31ndgCjH_3Y7-zz1t-wB62AZ-6Fan_qixUiKu')

sleep(10)
poco(focused="True").click()
sleep(5)
poco("com.android.vending:id/right_button").click()
sleep(3)
poco("com.android.vending:id/continue_button").click()
while True:
    if exists(Template(r"tpl1574303013068.png", record_pos=(0.001, -0.143), resolution=(1440, 2560))):
        break
    sleep(1)
stop_app('com.android.chrome')
sleep(3)
start_app(app_id)
sleep(20)
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# sleep(20)
# if exists(Template(r"tpl1572330183679.png", record_pos=(-0.301, 0.067), resolution=(1440, 2560))):
#     i=45
#     while True: 
#         if i==1:
#             break
#         poco.click([0.5,0.5])
#         sleep(1)
#         i-=1

# if exists(Template(r"tpl1572332351608.png", record_pos=(0.406, -0.634), resolution=(1440, 2560))):
               
#     touch(Template(r"tpl1572332351608.png", record_pos=(0.406, -0.634), resolution=(1440, 2560)))
#     sleep(3)             
# if exists(Template(r"tpl1572330507435.png", record_pos=(0.393, -0.601), resolution=(1440, 2560))):
#     touch(Template(r"tpl1572330507435.png", record_pos=(0.393, -0.601), resolution=(1440, 2560)))
#     sleep(3)
# if exists(Template(r"tpl1572330542556.png", record_pos=(-0.005, 0.722), resolution=(1440, 2560))):
#     touch(Template(r"tpl1572330542556.png", record_pos=(-0.005, 0.722), resolution=(1440, 2560)))
#     sleep(3)


# if exists(Template(r"tpl1572330625078.png", record_pos=(0.156, -0.757), resolution=(1440, 2560))):
#     poco.click([0.91,0.074])
#     sleep(3)
#     swipe(Template(r"tpl1572331137213.png", record_pos=(0.024, 0.632), resolution=(1440, 2560)), vector=[-0.0333, -0.1582])
    
#     if exists(Template(r"tpl1572331541614.png", record_pos=(0.042, 0.481), resolution=(1440, 2560))):
#         touch(Template(r"tpl1572331541614.png", record_pos=(0.042, 0.481), resolution=(1440, 2560)))
#         sleep(20)
#     elif exists(Template(r"tpl1572331587497.png", record_pos=(-0.251, 0.485), resolution=(1440, 2560))):
        
#         touch(Template(r"tpl1572331587497.png", record_pos=(-0.251, 0.485), resolution=(1440, 2560)))
#         sleep(20)
#     else:
#         pass
# if poco('一键购买').exists():
#     poco('一键购买').click()
#     sleep(10)
#     poco.click([0.5,0.5])
#     if exists(Template(r"tpl1572331735024.png", record_pos=(0.397, -0.625), resolution=(1440, 2560))):
#         touch(Template(r"tpl1572331735024.png", record_pos=(0.397, -0.625), resolution=(1440, 2560)))
#         sleep(3)
# stop_app(app_id)
# sleep(3)

    
            
    












    


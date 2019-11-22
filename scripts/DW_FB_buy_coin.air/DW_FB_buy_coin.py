# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *
login_mode ='facebook'
from utils import *
auto_setup(__file__)
#DoubleWin
def uninstall_DW():
    status = os.popen(
        'adb uninstall com.huge.slots.casino.vegas.android.avidly')
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
#######################################################
try:
    uninstall_DW()
except:
    Logging('DW命令异常---')
    pass
#安装doubolewin
try:
    install_DW()
except:
    log('DW安装失败')
    Logging('DW安装失败')
    pass
############################################################

app_id='com.huge.slots.casino.vegas.android.avidly'
start_app(app_id)
sleep(15)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
if exists(Template(r"tpl1572321674058.png", record_pos=(0.006, 0.219), resolution=(2560, 1440))):
    touch(Template(r"tpl1572321674058.png", record_pos=(0.006, 0.219), resolution=(2560, 1440)))
    sleep(3)
if login_mode=='facebook':
    if exists(Template(r"tpl1572321720658.png", record_pos=(0.018, 0.203), resolution=(2560, 1440))):
        touch(Template(r"tpl1572321720658.png", record_pos=(0.018, 0.203), resolution=(2560, 1440)))
        sleep(30)
else:
    if exists(Template(r"tpl1572321720658.png", record_pos=(0.018, 0.203), resolution=(2560, 1440))):
        poco.click([0.73, 0.85])
        sleep(30)

if exists(Template(r"tpl1572321920350.png", record_pos=(-0.004, 0.166), resolution=(2560, 1440))):
    touch(Template(r"tpl1572321920350.png", record_pos=(-0.004, 0.166), resolution=(2560, 1440)))
    sleep(5)
sleep(20)
i = 11
while True:
    i-=1
    if i==1:
        break
    keyevent("BACK")
    sleep(1)
    poco.click([0.04,0.16])
if exists(Template(r"tpl1572594865097.png", record_pos=(0.255, -0.192), resolution=(2560, 1440))):
    touch(Template(r"tpl1572594865097.png", record_pos=(0.255, -0.192), resolution=(2560, 1440)))

if exists(Template(r"tpl1572322763182.png", record_pos=(0.003, -0.247), resolution=(2560, 1440))) or exists(Template(r"tpl1573796173655.png", record_pos=(-0.041, -0.255), resolution=(2560, 1440))):#进入购买
    poco.click([0.43,0.034])
    sleep(5)
    if exists(Template(r"tpl1572322899475.png", record_pos=(0.318, -0.132), resolution=(2560, 1440))):
        touch(Template(r"tpl1572322899475.png", record_pos=(0.318, -0.132), resolution=(2560, 1440)))
        sleep(15)
        if poco('一键购买').exists():
            poco('一键购买').click()
            sleep(15)
            assert_exists(Template(r"tpl1572323059575.png", record_pos=(0.004, 0.192), resolution=(2560, 1440)))
            # if exists(Template(r"tpl1572323105855.png", record_pos=(0.398, -0.193), resolution=(2560, 1440))):
            #     touch(Template(r"tpl1572323105855.png", record_pos=(0.398, -0.193), resolution=(2560, 1440)))
            #     sleep(3)
            # if exists(Template(r"tpl1572323151167.png", record_pos=(0.433, -0.226), resolution=(2560, 1440))):
            #     touch(Template(r"tpl1572323151167.png", record_pos=(0.433, -0.226), resolution=(2560, 1440)))
            #     sleep(3)
stop_app(app_id)
sleep(5)
clear_app(app_id)

#######################################################################
from airtest.core.api import *

from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(10)


game_id = '600107'

sleep(3)
driver.maximize_window()
driver.get("http://tech-support.upltv.com:82/index")
driver.find_element_by_xpath("//a[@href='/auth/login']").click()

driver.find_element_by_xpath("//input[@autocomplete='on']").send_keys('Colin.chi@avid.ly')
driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys('Temp2019')
driver.find_element_by_xpath("//input[@value='登录']").click()
sleep(5)
Logging('准备数据上报------------------------------------------')
driver.find_element_by_xpath("//*[@id=\"bs-example-navbar-collapse-1\"]/ul/li/a/span").click()
driver.find_element_by_xpath("//a[@href='/report/analysis']").click()

driver.find_element_by_xpath("//input[@type='text']").send_keys(game_id)
sleep(3)
driver.find_element_by_xpath("//*[@id=\"contentlist\"]/li/span").click()
sleep(10)
Logging("获取数据")
driver.find_element_by_name("getdata").click()
sleep(10)
driver.find_element_by_name("getdata").click()
sleep(10)
driver.find_element_by_name("getdata").click()
sleep(10)
driver.execute_script('window.scrollTo(0,400)')
sleep(5)
driver.snapshot('****************************************************************')
driver.execute_script('window.scrollTo(0,800)')
sleep(5)
driver.snapshot('****************************************************************')
sleep(5)
#数据打点
Logging('准备数据打点------------------------------------------------')
driver.find_element_by_xpath("//*[@id=\"bs-example-navbar-collapse-1\"]/ul/li/a/span").click()
driver.find_element_by_xpath("//a[@href='/logdata/analysis']").click()



sleep(10)
driver.find_element_by_xpath("//input[@type='text']").send_keys(game_id)
sleep(3)
driver.find_element_by_xpath("//*[@id=\"contentlist\"]/li/span").click()
sleep(10)
driver.find_element_by_name("getdata").click()
sleep(10)
driver.snapshot('****************************************************************')
for i in range (10):
    driver.airtest_touch(Template(r"tpl1573711061814.png", record_pos=(1.429, 0.566), resolution=(913, 897)))
driver.snapshot('****************************************************************')
Logging("清空数据")
driver.find_element_by_name("cleardata").click()
sleep(5)
driver.snapshot()




    

        








     
        


    




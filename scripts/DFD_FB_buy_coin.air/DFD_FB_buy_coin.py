# -*- encoding=utf8 -*-
__author__ = "Colin"

from airtest.core.api import *
from utils import *
from constant import *
auto_setup(__file__)
def uninstall_DFD():
    status = os.popen(
        'adb uninstall com.defenders.android')
    list = status.readlines()
    if list[0].find('Success') >= 0:
        log('DFD卸载执行成功---')
        Logging('DFD卸载执行成功---')
    elif list[0].find('Failure') >= 0:
        log('DFD卸载失败---')
        Logging('DFD卸载失败---')
    else:
        log('DFD命令异常---')
        Logging('DFD命令异常---')
def pushObb():
    os.popen(DFD_PUSH,'w')
    install_DFD()

def install_DFD():
    app_path = DFD_APP
    Install = os.system(
        'adb install ' + app_path)
    # 构建成功安装APKS
    if Install == 0:
        log('DFD安装成功')
        Logging('DFD安装成功')
        sleep(2)

    else:
        log('DFD安装失败')
        Logging('DFD安装失败')
        pass
#######################################################################
try:
    uninstall_DFD()

except:
    Logging('DFD命令异常---')
    pass
sleep(10)
try:
    pushObb()
except:
    Logging('DFDpush命令异常---')
    pass


app_id='com.defenders.android'
start_app(app_id)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
sleep(15)
if exists(Template(r"tpl1574063904456.png", record_pos=(0.01, 0.205), resolution=(1440, 2560))):
    touch(Template(r"tpl1574063904456.png", record_pos=(0.01, 0.205), resolution=(1440, 2560)))
    
    sleep(20)
if exists(Template(r"tpl1574058825058.png", record_pos=(0.428, -0.398), resolution=(1440, 2560))):
    touch(Template(r"tpl1574058825058.png", record_pos=(0.428, -0.398), resolution=(1440, 2560)))
sleep(5)
poco.click([0.5,0.8])
sleep(5)

if exists(Template(r"tpl1574059020273.png", record_pos=(0.179, -0.848), resolution=(1440, 2560))):
    poco.click([0.66,0.025])
    sleep(5)
    if exists(Template(r"tpl1574063488989.png", record_pos=(0.008, 0.41), resolution=(1440, 2560))):
        touch(Template(r"tpl1574063488989.png", record_pos=(0.008, 0.41), resolution=(1440, 2560)))
        poco.click([0.66,0.025])
        sleep(5)
    if exists(Template(r"tpl1574059078084.png", record_pos=(0.287, 0.406), resolution=(1440, 2560))):
        touch(Template(r"tpl1574059078084.png", record_pos=(0.287, 0.406), resolution=(1440, 2560)))
    elif exists(Template(r"tpl1574059289983.png", record_pos=(0.303, 0.159), resolution=(1440, 2560))):
          touch(Template(r"tpl1574059289983.png", record_pos=(0.303, 0.159), resolution=(1440, 2560)))

sleep(15)
if poco('一键购买').exists():
    poco('一键购买').click()
    sleep(10)
sleep(5)
stop_app(app_id)
sleep(3)
clear_app(app_id)
#################################################################


from airtest.core.api import *
from airtest_selenium.proxy import WebChrome
game_id = '600180'
driver = WebChrome()
driver.implicitly_wait(20)
sleep(10)
driver.maximize_window()
sleep(10)
driver.get("http://tech-support.upltv.com:82/index")

driver.find_element_by_xpath("//a[@href='/auth/login']").click()

driver.find_element_by_xpath("//input[@autocomplete='on']").send_keys('Colin.chi@avid.ly')
driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys('Temp2019')
driver.find_element_by_xpath("//input[@value='登录']").click()
sleep(10)
Logging('准备数据上报------------------------------------------')
driver.find_element_by_xpath("//*[@id=\"bs-example-navbar-collapse-1\"]/ul/li/a/span").click()
driver.find_element_by_xpath("//a[@href='/report/analysis']").click()

driver.find_element_by_xpath("//input[@type='text']").send_keys(game_id)
sleep(10)
driver.find_element_by_xpath("//*[@id=\"contentlist\"]/li/span").click()
sleep(10)
Logging("获取数据")
driver.find_element_by_name("getdata").click()
sleep(5)
driver.find_element_by_name("getdata").click()
sleep(5)
driver.find_element_by_name("getdata").click()
sleep(5)
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

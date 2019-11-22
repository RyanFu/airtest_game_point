# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *
from utils import *
#DHM配置
login_mode ='facebook'
auto_setup(__file__)
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

try:
    uninstall_BB()
except:
    Logging('BB命令异常---')
    pass
#安装Binggoblaze
try:
    install_BB()
except:
    log('BB安装失败')
    Logging('BB安装失败')
    pass
#######################################################
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
sleep(3)
clear_app(app_id)

#############################################################################from airtest.core.api import *
from airtest_selenium.proxy import WebChrome
game_id = '600077'
driver = WebChrome()
driver.implicitly_wait(20)
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
sleep(5)
driver.find_element_by_name("getdata").click()
sleep(5)
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
driver.execute_script('window.scrollTo(0,400)')
sleep(5)
driver.snapshot('****************************************************************')
driver.execute_script('window.scrollTo(0,800)')
sleep(5)
driver.snapshot('****************************************************************')
Logging("清空数据")
driver.find_element_by_name("cleardata").click()
sleep(5)
driver.snapshot()









# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *
from utils import *
from constant import *
login_mode ='facebook'
auto_setup(__file__)
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

def install_BJ():
    app_path = "D:\\testdir\\Result\\bingojourney.apk"
    install = os.system(
        'adb install ' + app_path)
    # 构建成功安装APKS
    if install == 0:
        log('BJ安装成功')
        Logging('BJ安装成功')
        sleep(2)

    else:
        log('BJ安装失败')
        Logging('BJ安装失败')
        pass
##########################################################
try:
    uninstall_BJ()
except:
    Logging('BJ命令异常---')
    pass
#安装Binggojourny
try:
    install_BJ()
except:
    log('BJ安装失败')
    Logging('BJ安装失败')
    pass
##########################################################
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
        if exists(Template(r"tpl1572316650111.png", record_pos=(-0.344, -0.186), resolution=(2560, 1440))):
            log('购买成功')
            pass
stop_app(app_id)    
sleep(3)
clear_app(app_id)
################################################################
from airtest.core.api import *
from airtest_selenium.proxy import WebChrome
game_id = '600144'
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


    






    

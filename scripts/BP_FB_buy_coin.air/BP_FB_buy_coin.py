# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *
from  utils import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
login_mode ='facebook'
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
#binggoparty
def uninstall_BP():
    status = os.popen(
        'adb uninstall com.bingo.tour.party.crazy.free')
    list = status.readlines()
    if list[0].find('Success') >= 0:
        log('BP卸载执行成功---')
        Logging('BP卸载执行成功---')
    elif list[0].find('Failure') >= 0:
        log('BP卸载失败---')
        Logging('BP卸载失败---')
    else:
        log('BP命令异常---')
        Logging('BP命令异常---')

def install_BP():
    app_path = "D:\\testdir\\Result\\bingoparty.apk"
    Install = os.system(
        'adb install ' + app_path)
    # 构建成功安装APKS
    if Install == 0:
        log('BP安装成功')
        Logging('BP安装成功')
        sleep(2)

    else:
        log('BP安装失败')
        Logging('BP安装失败')
        pass
#######################################################################
try:
    uninstall_BP()
except:
    Logging('BP命令异常---')
    pass

try:
    install_BP()
except:
    log('BP安装失败')
    Logging('BP安装失败')
    pass
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
sleep(3)
clear_app(app_id)

############################################################################
from airtest.core.api import *
from airtest_selenium.proxy import WebChrome
game_id = '600056'
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
Logging("清空数据")
driver.find_element_by_name("cleardata").click()
sleep(5)
driver.snapshot()


            
    

    

       












    

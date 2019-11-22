# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *
from utils import *
auto_setup(__file__)

def uninstall_JJC():
    status = os.popen(
        'adb uninstall jelly.jam.fruit.match.cookie')
    list = status.readlines()
    if list[0].find('Success') >= 0:
        log('JJC卸载执行成功---')
        Logging('JJC卸载执行成功---')
    elif list[0].find('Failure') >= 0:
        log('JJC卸载失败---')
        Logging('JJC卸载失败---')
    else:
        log('JJC命令异常---')
        Logging('JJC命令异常---')
def install_JJC():
    time_tup = time.localtime(time.time())
    format_time = '%Y-%m-%d_%a_%H-%M-%S'
    apksName = time.strftime(format_time, time_tup)
    build_device_apks = 'D:\\testdir\\Result\\JJC_Release\\' + apksName + '.apks'
    # 通过AAB构建APKS----代替---install(apk_path)
    Build = os.system(
        'java -jar D:\\testdir\\lib\\bundletool-all-0.10.2.jar build-apks --connected-device --bundle=D:\\testdir\\Result\\JJC_Release\\JJC_Release.aab --output=' + build_device_apks + ' --ks=D:\\testdir\\lib\\signature.keystore --ks-pass=pass:123456 --ks-key-alias=key --key-pass=pass:123456')
    if Build == 0:
        log('JJC构建成功')
        Install = os.system(
            'java -jar D:\\testdir\\lib\\bundletool-all-0.10.2.jar install-apks --apks=' + build_device_apks)
        # 构建成功安装APKS
        if Install == 0:
            log('JJC安装成功')
            Logging('JJC安装成功')
            sleep(2)
        else:
            log('JJC安装失败')
            Logging('JJC安装失败')
            pass
    else:
        log('JJC构建失败')
        Logging('JJC构建失败')
try:
    uninstall_JJC()
except:
    log('JJC卸载失败')
    Logging('JJC卸载失败')
    pass
try:
    install_JJC()
except:
    log('JJC安装失败')
    Logging('JJC安装失败')
    pass
def buy_coin():
    if exists(Template(r"tpl1574322545633.png", record_pos=(0.442, -0.833), resolution=(1440, 2560))):
        
        touch(Template(r"tpl1574322545633.png", record_pos=(0.442, -0.833), resolution=(1440, 2560)))
        sleep(5)
        if exists(Template(r"tpl1574322835786.png", record_pos=(-0.24, -0.143), resolution=(1440, 2560))):
            touch(Template(r"tpl1574322835786.png", record_pos=(-0.24, -0.143), resolution=(1440, 2560)))
            sleep(29)
            poco("一键购买").click()
            sleep(10)
            poco.click([0.5,0.65])
        
app_id='jelly.jam.fruit.match.cookie'
start_app(app_id)
sleep(20)
if exists(Template(r"tpl1574322379680.png", record_pos=(-0.362, 0.77), resolution=(1440, 2560))):
    touch(Template(r"tpl1574322379680.png", record_pos=(-0.362, 0.77), resolution=(1440, 2560)))
    sleep(5)
    touch(Template(r"tpl1574322418799.png", record_pos=(-0.408, 0.789), resolution=(1440, 2560)))
    sleep(5)
    touch(Template(r"tpl1574322442946.png", record_pos=(-0.06, 0.79), resolution=(1440, 2560)))
    sleep(5)
    touch(Template(r"tpl1574322473516.png", record_pos=(0.399, -0.61), resolution=(1440, 2560)))
sleep(10)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
buy_coin()#购买金币
#########################################################
########################################################################
from airtest_selenium.proxy import WebChrome
game_id = '600112'
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
for i in range (10):
    driver.airtest_touch(Template(r"tpl1573711061814.png", record_pos=(1.429, 0.566), resolution=(913, 897)))
driver.snapshot('****************************************************************')
sleep(5)
Logging("清空数据")
driver.find_element_by_name("cleardata").click()
sleep(5)
driver.snapshot()

#########################################################
#facebook
if exists(Template(r"tpl1574323010154.png", record_pos=(-0.416, -0.658), resolution=(1440, 2560))):
    touch(Template(r"tpl1574323010154.png", record_pos=(-0.416, -0.658), resolution=(1440, 2560)))
    sleep(3)
    poco.click([0.72,0.15])
    sleep(3)
    poco.click([0.5,0.5])
    touch(Template(r"tpl1574323095174.png", record_pos=(-0.001, 0.092), resolution=(1440, 2560)))
    sleep(20)
    if exists(Template(r"tpl1574323204692.png", record_pos=(0.402, -0.58), resolution=(1440, 2560))):
        touch(Template(r"tpl1574323204692.png", record_pos=(0.402, -0.58), resolution=(1440, 2560)))
        poco.click([0.89,0.17])

    sleep(3)
    if exists(Template(r"tpl1574323291679.png", record_pos=(-0.012, 0.119), resolution=(1440, 2560))):
        touch(Template(r"tpl1574323291679.png", record_pos=(-0.012, 0.119), resolution=(1440, 2560)))
        sleep(5)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
buy_coin()#购买金币
#########################################################
########################################################################
from airtest_selenium.proxy import WebChrome
game_id = '600112'
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
for i in range (10):
    driver.airtest_touch(Template(r"tpl1573711061814.png", record_pos=(1.429, 0.566), resolution=(913, 897)))
driver.snapshot('****************************************************************')
sleep(5)
Logging("清空数据")
driver.find_element_by_name("cleardata").click()
sleep(5)
driver.snapshot()

 











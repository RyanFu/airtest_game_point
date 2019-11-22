# -*- encoding=utf8 -*-
__author__ = "chihai"

from airtest.core.api import *
from utils import *
auto_setup(__file__)
def uninstall_TBC():
    status = os.popen(
        'adb uninstall com.toybrickcrush.casual.avidly')
    list = status.readlines()
    if list[0].find('Success') >= 0:
        log('TBC卸载执行成功---')
        Logging('TBC卸载执行成功---')
    elif list[0].find('Failure') >= 0:
        log('TBC卸载失败---')
        Logging('TBC卸载失败---')
    else:
        log('TBC命令异常---')
        Logging('TBC\命令异常---')
def install_TBC():
    app_path ="D:\\testdir\\Result\\ToyBrickCrush.apk"
    Install = os.system(
        'adb install ' + app_path)
    # 构建成功安装APKS
    if Install == 0:
        log('TBC安装成功')
        Logging('TBC安装成功')
        sleep(2)

    else:
        log('TBC安装失败')
        Logging('TBC安装失败')
        pass
try:
    uninstall_TBC()
except:
    Logging('TBC命令异常---')
    pass

try:
    install_TBC()
except:
    log('TBC安装失败')
    Logging('TBC安装失败')
    pass
####################################################################
app_id ='com.toybrickcrush.casual.avidly'
start_app(app_id)
sleep(30)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco.click([0.49,0.58])
sleep(5)
touch(Template(r"tpl1571380055680.png", record_pos=(-0.05, -0.924), resolution=(1440, 2880)))
sleep(5)

if exists(Template(r"tpl1571380134096.png", record_pos=(0.265, 0.298), resolution=(1440, 2880))):
    touch(Template(r"tpl1571380134096.png", record_pos=(0.265, 0.298), resolution=(1440, 2880)))
    
elif exists(Template(r"tpl1571380226587.png", record_pos=(0.263, 0.714), resolution=(1440, 2880))):
    touch(Template(r"tpl1571380226587.png", record_pos=(0.263, 0.714), resolution=(1440, 2880)))
else:
    touch(Template(r"tpl1571380299942.png", record_pos=(0.201, -0.529), resolution=(1440, 2880)))
sleep(10)

if poco('一键购买').exists():
    poco('一键购买').click()
    sleep(15)
if exists(Template(r"tpl1571380941037.png", record_pos=(0.433, -0.947), resolution=(1440, 2880))):
    touch(Template(r"tpl1571380941037.png", record_pos=(0.433, -0.947), resolution=(1440, 2880)))
sleep(5)
stop_app(app_id)

########################################################################
from airtest_selenium.proxy import WebChrome
game_id = '600141'
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

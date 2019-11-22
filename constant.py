# -*- coding: utf-8 -*-
# Leo Zeng
import os

BASEPATH = os.path.abspath('.')
LOG_ROOT = os.path.join(BASEPATH, 'logs_root')#BASEPATH=D:\airtest_runner-master
CFG_SCRIPTS_ROOT = 'scripts_root'
CFG_SCRIPTS = 'scripts'
CFG_DEVICES = 'devices'
CFG_MODE = 'mode'
CFG_PLATFORM = 'platform'

DFD_PUSH="adb push D:\\testdir\\Result\\DFD_Release\\main.10023.com.defenders.android.obb  /sdcard/Android/obb/com.defenders.android/main.10023.com.defenders.android.obb"
DFD_APP="D:\\testdir\\Result\\DFD_Release\\main.10023.com.defenders.android.apk"

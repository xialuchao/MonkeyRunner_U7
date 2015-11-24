#coding =utf-8
__author__ = 'shylock'
import time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage


class dev():
    print "Connect the device...."
    device = MonkeyRunner.waitForConnection()
    print 'Device is connected!'
#coding = utf-8
__author__ = 'shylock'
import sys
sys.path.append('E:\\testing\\MonkeyRunner_U7')
import time
import os
from config import dev
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import script1
import script2
dev()
if __name__ == '__main__':
    # now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    # pathlog = 'E:\\testing\\script_total\\' + now + '.log'
    # log = open(pathlog,'w')
    # sys.stdout = log
    # sys.path.append(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0]))))
    TestTimes = 10000
    Test_Count = 1
    while Test_Count < TestTimes:
        print "------Test is Beginning! TestTimes:%d------" %Test_Count
        print (time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
        script1.scripta(Test_Count)
        script2.scriptb(Test_Count)
        dev.device.drag((886,0),(886,1800),1,10)
        MonkeyRunner.sleep(1)
        dev.device.drag((886,1600),(886,800),1,10)
        MonkeyRunner.sleep(1)
        dev.device.drag((886,1600),(886,800),1,10)
        MonkeyRunner.sleep(1)
        dev.device.drag((886,1600),(886,800),1,10)
        MonkeyRunner.sleep(1)
        dev.device.touch(984,1668,'DOWN_AND_UP')
        MonkeyRunner.sleep(1)
        dev.device.press('KEYCOD_BACK','DOWN_AND_UP')
        MonkeyRunner.sleep(1)
        Test_Count = Test_Count + 1
    # log.close()

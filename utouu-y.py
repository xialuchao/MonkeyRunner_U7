# -*- coding = unicode -*-
import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0]))))
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice,By               
from com.android.monkeyrunner.recorder import MonkeyRecorder as myrecorder 

print "Connect the device...."
device = MonkeyRunner.waitForConnection()
print 'Device is connected!'



TestTimes = 2
Test_Count = 1
while Test_Count < TestTimes:
	print "------Test is Beginning! TestTimes:%d------" %Test_Count 
	print(time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
	MonkeyRunner.sleep(1) 
	
	# ###########################################Calculator###############################################################
	# device.touch(947,1784,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(422,223,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# print 'Enter the calculator interface'
	#
	# device.touch(161,1474,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '1'
	# MonkeyRunner.sleep(1)
	#
	#
	# device.touch(398,1455,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '2'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(658,1455,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '3'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(180,1160,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '4'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(410,1160,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '5'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(650,1160,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '6'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(160,918,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '7'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(426,918,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '8'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(631,918,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '9'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(397,1733,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '0'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(886,850, 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Delete'
	# MonkeyRunner.sleep(1)
	#
	# device.drag((886,850),(886,850),1,10)
	# MonkeyRunner.sleep(1)
	# print 'Reset'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(161,1474,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '1'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(169,1760,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '.'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(410,1160,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '5'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(909,1739,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '+'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(426,918,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '8'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(638,1755,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '='
	# MonkeyRunner.sleep(1)
	#
	# device.touch(921,1512,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '-'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(658,1455,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '3'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(638,1755,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '='
	# MonkeyRunner.sleep(1)
	#
	# device.touch(909,1310,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'x'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(410,1160,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '5'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(638,1755,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '='
	# MonkeyRunner.sleep(1)
	#
	# device.touch(903,1085,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '/'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(631,918,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '9'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(638,1755,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print '='
	# MonkeyRunner.sleep(2)
	#
	# device.drag((886,850),(886,850),1,10)
	# MonkeyRunner.sleep(1)
	# print 'Reset'
	# MonkeyRunner.sleep(1)
	#
	# device.drag((1019,1285),(160,1285),1,10)
	# MonkeyRunner.sleep(1)
	# print 'mathematical symbol'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(418,910,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
    #
	# device.touch(667,921,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.touch(897,912,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.touch(393,1190,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.touch(653,1176,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.touch(900,1205,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.touch(426,1430,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
    #
	# device.touch(667,1459,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.touch(908,1472,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.touch(457,1715,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.touch(663,1736,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.touch(915,1726,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.drag((300,1351),(1008,1351),1,10)
	# MonkeyRunner.sleep(1)
	# print 'Calculator interface'
	# MonkeyRunner.sleep(1)
	#
	# device.drag((886,850),(886,850),1,10)
	# MonkeyRunner.sleep(1)
	# print 'Reset'
	# MonkeyRunner.sleep(1)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.press('KEYCODE_HOME','DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# ########################################### Clock #########################################################################
	# device.touch(929,1389,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(155,161,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# print 'Enter the Clock'
	#
	# #Case 1
	# device.touch(539,1795,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Create an alarm clock'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(761,1052,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(783,912,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Set 03:10'
	# MonkeyRunner.sleep(1)
	# device.touch(826,1562,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(990,425,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Turn off the alarm clock'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(132,1078,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Delete'
	# MonkeyRunner.sleep(3)
	#
	# #Case 2
	# device.touch(331,430,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Modify the time'
	# MonkeyRunner.sleep(1)
	# device.touch(830,1559,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(128,762,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(985,738,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Set REPEAT'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(256,890,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(235,930,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Set the BELL'
	# MonkeyRunner.sleep(2)
	# device.touch(885,1776,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(869,896,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Set the VIBRATION'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(178,1036,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('AaBbCc123456')
	# MonkeyRunner.sleep(3)
	# device.touch(753,780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(1009,405,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 3
	# device.touch(389,152,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(540,1789,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(215,500,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Choose City'
	# MonkeyRunner.sleep(1)
	# device.touch(70,167,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# #Case 4
	# device.touch(1035,1803,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(798,1509,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Enter Night Mode'
	# MonkeyRunner.sleep(5)
	# device.touch(776,765,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 5
	# device.touch(692,150,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(560,755,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(881,750,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(560,1027,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(259,1277,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(537,1565,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.touch(543,1778,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Start Countdown'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(519,1790,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Stop'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(558,1163,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Reset'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(527,685,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('AaBbCc123456')
	# MonkeyRunner.sleep(3)
	# device.touch(753,780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(185,1769,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Delete'
	# MonkeyRunner.sleep(2)
	#
	# #Case 5
	# device.touch(956,150,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(527,1787,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Start Stopwatch'
	# MonkeyRunner.sleep(5)
	#
	# device.touch(527,1787,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Stop'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(877,1787,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Share'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(212,1662,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Share via Message'
	# MonkeyRunner.sleep(3)
	# device.touch(81,151,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(847,1167,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(877,1787,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Share'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(272,1838,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Share via BT'
	# MonkeyRunner.sleep(3)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(178,1783,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.press('KEYCODE_HOME','DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# ################################################Camera###########################################################
	# device.touch(150,1025,'DOWN_AND_UP')
	# MonkeyRunner.sleep(5)
	#
	# #Case 1
	# device.touch(668,1782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(3)
	#
	# device.touch(1003,1361,'DOWN_AND_UP')
	# print 'Flash'
	# MonkeyRunner.sleep(5)
	# device.touch(668,1782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(3)
	#
	# device.touch(998,1212,'DOWN_AND_UP')
	# print 'HDR'
	# MonkeyRunner.sleep(5)
	# device.touch(668,1782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(3)
	#
	# device.touch(1025,1511,'DOWN_AND_UP')
	# print 'HDR'
	# MonkeyRunner.sleep(5)
	# device.touch(668,1782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(3)
	#
	# device.drag((668,1782),(668,1782),5,10)
	# MonkeyRunner.sleep(3)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# # Case 2
	# device.touch(150,1025,'DOWN_AND_UP')
	# MonkeyRunner.sleep(5)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Videotape'
	# MonkeyRunner.sleep(6)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
    #
	# device.touch(1003,1361,'DOWN_AND_UP')
	# print 'Flash'
	# MonkeyRunner.sleep(5)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Videotape'
	# MonkeyRunner.sleep(6)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.touch(998,1212,'DOWN_AND_UP')
	# print 'HDR'
	# MonkeyRunner.sleep(5)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(6)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.touch(1025,1511,'DOWN_AND_UP')
	# print 'HDR'
	# MonkeyRunner.sleep(5)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(6)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
    #
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 3
	# device.touch(150,1025,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(129,1788,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Settings'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(877,695,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'GPS'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(820,856,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(882,915,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Exposure'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(926,1126,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(885,828,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'White Balance'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(927,1315,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(432,725,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Image properties'
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.drag((650,1283),(650,839),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(920,1222,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(886,866,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Anti-Flicker'
	# MonkeyRunner.sleep(1)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.touch(668,1782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(3)
	#
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Videotape'
	# MonkeyRunner.sleep(6)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 4
	# device.touch(150,1025,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(129,1788,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Settings'
	# MonkeyRunner.sleep(1)
	# device.touch(480,552,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(852,700,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Zero Shutter Delay'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(869,843,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Anti-Shake'
	# MonkeyRunner.sleep(2)
	#
	# device.drag((728,1313),(728,632),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(880,952,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(885,913,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Picture Size'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(888,1113,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(887,1022,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Preview Size'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(903,1216,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(887,828,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'ISO'
	# MonkeyRunner.sleep(2)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.touch(668,1782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(3)
	#
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Videotape'
	# MonkeyRunner.sleep(6)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 5
	# device.touch(150,1025,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(129,1788,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Settings'
	# MonkeyRunner.sleep(1)
	# device.touch(480,552,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(932,1317,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(889,947,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Self Timer'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(878,1005,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Face Detection'
	# MonkeyRunner.sleep(2)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.touch(668,1782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(6)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 6
	# device.touch(150,1025,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(129,1788,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Settings'
	# MonkeyRunner.sleep(1)
	# device.touch(872,552,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(830,700,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Noise Reduction'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(877,855,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'EIS'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(903,1167,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(879,879,'DOWN_AND_UP')
	# print 'Audio Mode'
	# MonkeyRunner.sleep(2)
	#
	# device.drag((696,1329),(696,818),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(925,1372,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(883,873,'DOWN_AND_UP')
	# print 'Video Quality'
	# MonkeyRunner.sleep(2)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Videotape'
	# MonkeyRunner.sleep(6)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.touch(129,1788,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Settings'
	# MonkeyRunner.sleep(1)
	# device.touch(255,552,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.drag((650,1283),(650,839),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(575,1361,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(762,1062,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 7
	# device.touch(150,1025,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(1018,1516,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(668,1782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(3)
	#
	# device.touch(990,1351,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'HDR'
	# MonkeyRunner.sleep(3)
	# device.touch(668,1782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(3)
	#
	# device.touch(990,1351,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'HDR'
	# MonkeyRunner.sleep(3)
	# device.touch(668,1782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(3)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 8
	# device.touch(150,1025,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(1018,1516,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Videotape'
	# MonkeyRunner.sleep(6)
	#
	#
	# device.touch(990,1351,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'HDR'
	# MonkeyRunner.sleep(3)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Videotape'
	# MonkeyRunner.sleep(6)
	#
	# device.touch(990,1351,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'HDR'
	# MonkeyRunner.sleep(3)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Videotape'
	# MonkeyRunner.sleep(6)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 9
	# device.touch(150,1025,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(1018,1516,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.touch(129,1788,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Settings'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(877,695,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'GPS'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(820,856,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(882,915,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Exposure'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(926,1126,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(885,828,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'White Balance'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(927,1315,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(432,725,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Image properties'
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.drag((650,1283),(650,839),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(920,1222,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(886,866,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Anti-Flicker'
	# MonkeyRunner.sleep(1)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.touch(668,1782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(3)
	#
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Videotape'
	# MonkeyRunner.sleep(6)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 10
	# device.touch(150,1025,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(1018,1516,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.touch(129,1788,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Settings'
	# MonkeyRunner.sleep(1)
	# device.touch(480,552,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(852,700,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Zero Shutter Delay'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(869,843,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Anti-Shake'
	# MonkeyRunner.sleep(2)
	#
	# device.drag((728,1313),(728,632),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(880,952,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(885,913,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Picture Size'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(888,1113,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(887,1022,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Preview Size'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(903,1216,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(887,828,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'ISO'
	# MonkeyRunner.sleep(2)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.touch(668,1782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(3)
	#
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Videotape'
	# MonkeyRunner.sleep(6)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 11
	# device.touch(150,1025,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(1018,1516,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.touch(129,1788,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Settings'
	# MonkeyRunner.sleep(1)
	# device.touch(480,552,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(932,1317,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(889,947,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Self Timer'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(878,1005,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Face Detection'
	# MonkeyRunner.sleep(2)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.touch(668,1782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Photograph'
	# MonkeyRunner.sleep(6)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 12
	# device.touch(150,1025,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(1018,1516,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.touch(129,1788,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Settings'
	# MonkeyRunner.sleep(1)
	# device.touch(872,552,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(830,700,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Noise Reduction'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(877,855,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'EIS'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(903,1167,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(879,879,'DOWN_AND_UP')
	# print 'Audio Mode'
	# MonkeyRunner.sleep(2)
	#
	# device.drag((696,1329),(696,818),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(925,1372,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(883,873,'DOWN_AND_UP')
	# print 'Video Quality'
	# MonkeyRunner.sleep(2)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Videotape'
	# MonkeyRunner.sleep(6)
	# device.touch(430,1780,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.touch(129,1788,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Settings'
	# MonkeyRunner.sleep(1)
	# device.drag((650,1283),(650,839),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(575,1361,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(762,1062,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Restore Defaults'
	# MonkeyRunner.sleep(2)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_HOME','DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	
	# device.touch(413,1029,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# print 'Enter the File Manager'
	# device.touch(613,310,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(355,1069,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(510,458,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.drag((598,316),(598,316),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(362,150,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(388,297,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.drag((602,1325),(602,269),2,10)
	# MonkeyRunner.sleep(1)
	# device.drag((602,1325),(602,269),2,10)
	# MonkeyRunner.sleep(1)
	# device.drag((602,1325),(602,269),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(307,708,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(512,1853,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(883,1146,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_HOME','DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# ###################################################SMS###########################################################
	# device.touch(927,1030,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 1
	# device.touch(850,137,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Search'
	# MonkeyRunner.sleep(1)
	# device.touch(293,155,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('abc')
	# MonkeyRunner.sleep(2)
	# print 'abc'
	# MonkeyRunner.sleep(1)
	# device.touch(1000,1813,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'No Matches'
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# device.touch(850,137,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Search'
	# MonkeyRunner.sleep(1)
	# device.touch(293,155,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('106558')
	# MonkeyRunner.sleep(2)
	# print '106558'
	# MonkeyRunner.sleep(1)
	# device.touch(1000,1813,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Result for 106558'
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 3
	# device.touch(700,156,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'New Message'
	# MonkeyRunner.sleep(1)
	# device.touch(987,313,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(137,350,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(725,166,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Add Contact 1'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(672,313,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('18621061090')  #type testing number
	# MonkeyRunner.sleep(1)
	# print 'Add Contact 2'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(350,1156,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('10010')
	# MonkeyRunner.sleep(1)
	#
	# device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(390,1383,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(516,386,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Insert Quick Text'
	# MonkeyRunner.sleep(1)
    #
	# device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(390,1560,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(366,336,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(855,168,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Insert Contact'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(1008,1838,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Send Message'
	# MonkeyRunner.sleep(15)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 5
	# device.touch(611,362,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(823,160,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(566,1812,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Dial'
	# MonkeyRunner.sleep(5)
	# device.touch(190,525,'DOWN_AND_UP')
	# MonkeyRunner.sleep(5)
	# device.touch(539,1758,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
    #
	#
	# #Case 7
	# #device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	# #MonkeyRunner.sleep(1)
	# #device.touch(522,1851,'DOWN_AND_UP')
	# #MonkeyRunner.sleep(1)
	# #print 'Chat Settings'
	# #MonkeyRunner.sleep(1)
	# #device.touch(339,410,'DOWN_AND_UP')
	# #MonkeyRunner.sleep(1)
	# #device.touch(760,830,'DOWN_AND_UP')
	# #MonkeyRunner.sleep(1)
	# #device.touch(873,459,'DOWN_AND_UP')
	# #MonkeyRunner.sleep(2)
	# #device.touch(201,420,'DOWN_AND_UP')
	# #MonkeyRunner.sleep(1)
	# #print 'Chat Wallpaper'
	# MonkeyRunner.sleep(1)
	# #device.touch(961,685,'DOWN_AND_UP')
	# #MonkeyRunner.sleep(1)
	# #device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# #MonkeyRunner.sleep(1)
	#
	# #Case 8
	# #device.touch(355,361,'DOWN_AND_UP')
	# #MonkeyRunner.sleep(1)
	# device.drag((191,1426),(191,1426),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(292,638,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Copy'
	# MonkeyRunner.sleep(1)
	# device.drag((298,1810),(298,1810),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(123,1706,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Paste'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(381,1833,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.drag((1012,1657),(1012,1657),3,10)
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# #Case 9
	# device.touch(355,361,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.drag((191,1426),(191,1426),2,10)
	# MonkeyRunner.sleep(2)
	# device.touch(320,705,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Forward'
	# MonkeyRunner.sleep(2)
	# device.touch(233,276,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('10010')
	# MonkeyRunner.sleep(2)
	# device.touch(1008,1165,'DOWN_AND_UP')
	# MonkeyRunner.sleep(8)
	#
	# #Case 10
	# device.touch(355,361,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.drag((191,1426),(191,1426),2,10)
	# MonkeyRunner.sleep(2)
	# device.touch(281,872,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(883,1145,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Delete'
	# MonkeyRunner.sleep(2)
	#
	# #Case 11
	# device.drag((178,1402),(178,1402),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(289,972,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Locked'
	# MonkeyRunner.sleep(2)
	#
	# device.drag((178,1402),(178,1402),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(289,972,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Unlocked'
	# MonkeyRunner.sleep(2)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.press('KEYCODE_HOME','DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #################################################MMS################################################################
	# device.touch(927,1030,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 1
	# device.touch(700,156,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'New Message'
	# MonkeyRunner.sleep(1)
	# device.touch(987,313,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(137,350,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(725,166,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Add Contact 1'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(672,313,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('18621058052')
	# MonkeyRunner.sleep(1)
	# print 'Add Contact 2'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(350,1156,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('10010')
	# MonkeyRunner.sleep(1)
	#
	# device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(390,1383,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(516,386,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Insert Quick Text'
	# MonkeyRunner.sleep(1)
    #
	# device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(390,1560,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(366,336,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(855,168,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Insert Contact'
	# MonkeyRunner.sleep(1)
	#
	# device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(596,1696,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Add Subject'
	# MonkeyRunner.sleep(2)
	# device.touch(383,481,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('NewMessage' + str(Test_Count))
	# MonkeyRunner.sleep(2)
	# device.touch(329,1122,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('Content' + str(Test_Count))
	# MonkeyRunner.sleep(2)
	# device.touch(855,168,'DOWN_AND_UP')
    #
	#
	# device.touch(999,1043,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Send Message'
	# MonkeyRunner.sleep(8)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# #Case 2
	# device.touch(700,156,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'New Message'
	# MonkeyRunner.sleep(1)
	# device.touch(672,313,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('18621058052')
	# MonkeyRunner.sleep(1)
	# print 'Add Contact 18621058052'
	# MonkeyRunner.sleep(1)
	# device.touch(63,1131,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(151,1406,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(523,340,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Add Pictures'
	# MonkeyRunner.sleep(2)
	#
	#
	# device.touch(72,1821,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(378,1391,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(539,1779,'DOWN_AND_UP')
	# MonkeyRunner.sleep(5)
	# device.touch(669,1782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Add Capture Picture'
	# MonkeyRunner.sleep(5)
	#
	# device.touch(882,1593,'DOWN_AND_UP')
	# MonkeyRunner.sleep(8)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	#
	# #Case 3
	# device.touch(167,1031,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(853,555,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.drag((387,1351),(387,920),2,10)
	# MonkeyRunner.sleep(1)
	# device.touch(287,1361,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(889,713,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(470,1787,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Capture Picture'
	# MonkeyRunner.sleep(3)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.press('KEYCODE_HOME','DOWN_AND_UP')
	#
	# device.touch(927,1030,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(700,156,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'New Message'
	# MonkeyRunner.sleep(1)
	# device.touch(672,313,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('18621058052')
	# MonkeyRunner.sleep(1)
	# print 'Add Contact 18621058052'
	# MonkeyRunner.sleep(1)
	# device.touch(63,1131,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(679,1409,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(587,338,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Add Videos'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(72,1821,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(932,1382,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(539,1779,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(539,1779,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(668,1785,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# #device.touch(660,1787,'DOWN_AND_UP')
	# #MonkeyRunner.sleep(1)
	# print 'Add Capture Picture'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(882,1593,'DOWN_AND_UP')
	# MonkeyRunner.sleep(8)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# #device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# #MonkeyRunner.sleep(2)
	#
	# #Case 4
	# device.touch(700,156,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'New Message'
	# MonkeyRunner.sleep(1)
	# device.touch(672,313,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('18621058052')
	# MonkeyRunner.sleep(1)
	# print 'Add Contact 18621058052'
	# MonkeyRunner.sleep(1)
	# device.touch(63,1131,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(153,1692,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(537,999,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(221,357,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(880,1773,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Add Audio'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(72,1821,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(427,1676,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(288,1830,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# device.touch(790,1828,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(826,1663,'DOWN_AND_UP')
	# MonkeyRunner.sleep(3)
	# print 'Add Record Audio'
	# MonkeyRunner.sleep(2)
	#
	# device.touch(882,1593,'DOWN_AND_UP')
	# MonkeyRunner.sleep(8)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# #device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# #MonkeyRunner.sleep(2)
    #
	# #Case 5
	# device.touch(700,156,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'New Message'
	# MonkeyRunner.sleep(1)
	# device.touch(672,313,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('18621058052')
	# MonkeyRunner.sleep(1)
	# print 'Add Contact 18621058052'
	# MonkeyRunner.sleep(1)
	# device.touch(63,1131,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(667,1658,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.touch(150,332,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(102,560,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(866,172,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Add Contact'
	# MonkeyRunner.sleep(1)
	#
	# device.touch(953,1832,'DOWN_AND_UP')
	# MonkeyRunner.sleep(8)
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# #device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# #MonkeyRunner.sleep(2)
	#
	# #Case 6
	# device.touch(616,353,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.drag((793,1629),(793,1629),2,10)
	# MonkeyRunner.sleep(2)
	# device.touch(368,782,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Forward'
	# MonkeyRunner.sleep(1)
	# device.touch(287,286,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.type('18621058052')
	# MonkeyRunner.sleep(2)
	# device.touch(922,1160,'DOWN_AND_UP')
	# MonkeyRunner.sleep(8)
	#
	# #Case 7
	# device.touch(616,353,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.drag((793,1629),(793,1629),2,10)
	# MonkeyRunner.sleep(2)
	# device.touch(592,857,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(866,1150,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Delete'
	# MonkeyRunner.sleep(1)
	#
	# #Case 8
	# device.touch(616,353,'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	# device.drag((793,1629),(793,1629),2,10)
	# MonkeyRunner.sleep(2)
	# device.touch(519,1280,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# device.touch(1012,153,'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	# print 'Save Attachment'
	# MonkeyRunner.sleep(2)
    #
	# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(1)
	#
	# device.press('KEYCODE_HOME','DOWN_AND_UP')
	# MonkeyRunner.sleep(2)
	#
	# ################################################File Manager#####################################################
	device.touch(413,1029,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'Enter the File Manager'

	device.touch(613,310,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	#Case 1
	device.touch(113,1839,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'New folder'
	MonkeyRunner.sleep(1)

	device.touch(261,566,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.type('NewFolder')
	MonkeyRunner.sleep(3)

	device.touch(867,807,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	device.drag((290,1100),(290,1100),2,10)
	MonkeyRunner.sleep(1)
	device.touch(551,1835,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.touch(870,1146,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Delete NewFolder'
	MonkeyRunner.sleep(1)



	#Case 2
	device.touch(553,1852,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Searching'
	MonkeyRunner.sleep(1)

	device.touch(358,167,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.type('Alarms')
	MonkeyRunner.sleep(3)

	device.touch(1003,1832,'DOWN_AND_UP')
	MonkeyRunner.sleep(3)

	device.touch(66,155,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Quit'
	MonkeyRunner.sleep(1)

	#Case 4
	device.drag((523,468),(523,1733),1,10)
	MonkeyRunner.sleep(1)
	device.touch(476,1363,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.touch(578,300,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.touch(578,300,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	device.drag((400,308),(400,308),2,10)
	MonkeyRunner.sleep(1)


	device.touch(73,1848,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.touch(578,300,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Sharing'
	MonkeyRunner.sleep(5)
	device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 5
	device.drag((206,308),(206,308),2,10)
	MonkeyRunner.sleep(1)
	device.touch(290,160,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.touch(318,292,'DOWN_AND_UP')
	MonkeyRunner.sleep(3)
	device.touch(58,160,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 6
	device.drag((523,468),(523,1733),1,10)
	MonkeyRunner.sleep(1)
	device.drag((215,1073),(215,1073),2,10)
	MonkeyRunner.sleep(1)
	device.touch(320,1839,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Copy'
	MonkeyRunner.sleep(2)
	device.touch(382,1846,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Paste'
	MonkeyRunner.sleep(2)

	device.drag((196,1213),(196,1213),2,10)
	MonkeyRunner.sleep(1)
	device.touch(552,1848,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.touch(875,1148,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 8
	device.touch(215,1073,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.touch(208,477,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.drag((310,310),(310,310),2,10)
	MonkeyRunner.sleep(1)
	device.touch(770,1846,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Cut'
	MonkeyRunner.sleep(1)
	device.touch(460,159,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.touch(417,1849,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Paste'
	MonkeyRunner.sleep(2)

	device.drag((352,618),(352,618),2,10)
	MonkeyRunner.sleep(1)
	device.touch(770,1846,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Cut'
	MonkeyRunner.sleep(1)
	device.touch(329,435,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.touch(417,1849,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Paste'
	MonkeyRunner.sleep(2)

	device.touch(220,156,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 9
	device.drag((235,1673),(235,1673),2,10)
	MonkeyRunner.sleep(1)
	device.touch(986,1855,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.touch(609,1706,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Rename'
	MonkeyRunner.sleep(1)
	device.touch(567,643,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.drag((1010,1607),(1010,1607),2,10)
	MonkeyRunner.sleep(1)
	device.type('Movies'+ str(Test_Count))
	MonkeyRunner.sleep(2)
	device.touch(876,822,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 10
	device.drag((199,1509),(199,1509),2,10)
	MonkeyRunner.sleep(1)
	device.touch(986,1855,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.touch(610,1852,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Details'
	MonkeyRunner.sleep(3)
	device.touch(860,1302,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	device.touch(43,150,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	device.press('KEYCODE_BACK','DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.press('KEYCODE_BACK','DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.press('KEYCODE_BACK','DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.press('KEYCODE_BACK','DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.press('KEYCODE_BACK','DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.press('KEYCODE_BACK','DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	device.press('KEYCODE_BACK','DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	device.press('KEYCODE_HOME','DOWN_AND_UP')
	MonkeyRunner.sleep(2)


	Test_Count = Test_Count+1


# -*- coding = unicode -*-
# -*- coding = gbk -*-
#coding =utf-8

from config import dev
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage


def scriptb(Test_Count):
####################call########################
	dev.device.touch(150,1788,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	#Case 1
	dev.device.touch(535,1808,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Telephone Dial'
	MonkeyRunner.sleep(2)

	dev.device.touch(236,998,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(236,998,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print '10010'
	MonkeyRunner.sleep(1)
	dev.device.touch(539,1800,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Dial'
	MonkeyRunner.sleep(2)
	dev.device.touch(202,531,'DOWN_AND_UP')
	MonkeyRunner.sleep(12)
	dev.device.touch(539,1800,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 2
	dev.device.touch(150,1788,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(535,1808,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Telephone Dial'
	MonkeyRunner.sleep(2)
	dev.device.touch(236,998,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print '1'
	MonkeyRunner.sleep(1)
	dev.device.touch(553,1023,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print '2'
	MonkeyRunner.sleep(1)
	dev.device.touch(859,1023,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print '3'
	MonkeyRunner.sleep(1)
	dev.device.touch(258,1201,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print '4'
	MonkeyRunner.sleep(1)
	dev.device.touch(535,1197,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print '5'
	MonkeyRunner.sleep(1)
	dev.device.touch(852,1199,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print '6'
	MonkeyRunner.sleep(1)
	dev.device.touch(236,1393,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print '7'
	MonkeyRunner.sleep(1)
	dev.device.touch(536,1382,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print '8'
	MonkeyRunner.sleep(1)
	dev.device.touch(851,1378,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print '9'
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print '0'
	MonkeyRunner.sleep(1)

	dev.device.drag((1017,795),(1017,795),2,10)
	MonkeyRunner.sleep(2)

	dev.device.touch(236,998,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(236,998,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(851,1378,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(851,1378,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(1017,795,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(1017,795,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print '10010'
	MonkeyRunner.sleep(1)

	dev.device.touch(539,1800,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Dial'
	MonkeyRunner.sleep(2)
	dev.device.touch(202,531,'DOWN_AND_UP')
	MonkeyRunner.sleep(12)
	dev.device.touch(539,1800,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 3
	dev.device.touch(150,1788,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(535,1808,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Telephone Dial'
	MonkeyRunner.sleep(2)

	dev.device.touch(236,998,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(536,1382,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(852,1199,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.touch(67,800,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(67,800,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(539,333,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(337,532,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.type('CMService' + str(Test_Count))
	MonkeyRunner.sleep(2)
	dev.device.touch(120,171,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Add 10086 to Contact'
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.touch(393,1787,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Enter Contacts'
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(671,166,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(265,338,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(850,165,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(835,1158,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Delete One Contact'
	MonkeyRunner.sleep(1)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 5
	dev.device.touch(150,1788,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(535,1808,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Telephone Dial'
	MonkeyRunner.sleep(2)

	dev.device.touch(236,998,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(236,998,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print '10010'
	MonkeyRunner.sleep(1)

	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(276,1368,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(316,1777,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.type('10010')
	MonkeyRunner.sleep(2)
	dev.device.touch(1003,1040,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Send SMS'
	MonkeyRunner.sleep(6)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 6
	#dev.device.touch(150,1788,'DOWN_AND_UP')
	#MonkeyRunner.sleep(2)
	#dev.device.touch(535,1808,'DOWN_AND_UP')
	#MonkeyRunner.sleep(1)
	#print 'Telephone Dial'
	#MonkeyRunner.sleep(2)
	#dev.device.drag((236,998),(236,998),2,10)
	#MonkeyRunner.sleep(1)
	#print 'Enter Voice Mail'
	#MonkeyRunner.sleep(3)
	#dev.device.touch(202,531,'DOWN_AND_UP')
	#MonkeyRunner.sleep(5)
	#dev.device.touch(539,1800,'DOWN_AND_UP')
	#MonkeyRunner.sleep(1)
	#dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	#MonkeyRunner.sleep(1)

	#Case 7
	dev.device.touch(150,1788,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(535,1808,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Telephone Dial'
	MonkeyRunner.sleep(2)
	dev.device.drag((553,1023),(553,1023),2,10)
	MonkeyRunner.sleep(1)
	print 'Dial Speed Number'
	MonkeyRunner.sleep(3)
	dev.device.touch(202,531,'DOWN_AND_UP')
	MonkeyRunner.sleep(5)
	dev.device.touch(539,1800,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 8
	dev.device.touch(150,1788,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(535,1808,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Telephone Dial'
	MonkeyRunner.sleep(2)

	dev.device.touch(236,998,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(236,998,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print '10010'
	MonkeyRunner.sleep(1)
	dev.device.touch(539,1800,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Dial'
	MonkeyRunner.sleep(2)

	dev.device.touch(202,531,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Turn on Speaker'
	MonkeyRunner.sleep(3)
	dev.device.touch(202,531,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Turn off Speaker'
	MonkeyRunner.sleep(1)


	dev.device.touch(377,520,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Mute'
	MonkeyRunner.sleep(2)
	dev.device.touch(377,520,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Unmute'
	MonkeyRunner.sleep(1)

	dev.device.touch(252,949,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(530,530,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(530,530,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Hide Dialer'
	MonkeyRunner.sleep(1)

	dev.device.touch(900,537,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(803,809,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Start Recording'
	MonkeyRunner.sleep(2)
	dev.device.touch(900,537,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(803,809,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Stop Recording'
	MonkeyRunner.sleep(1)

	dev.device.touch(900,537,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(773,666,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Add Call'
	MonkeyRunner.sleep(1)
	dev.device.touch(236,998,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,1575,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(536,1382,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(852,1199,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(539,1800,'DOWN_AND_UP')
	MonkeyRunner.sleep(3)


	dev.device.touch(532,1649,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(539,1800,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 9
	dev.device.touch(150,1788,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(551,627,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Call History'
	MonkeyRunner.sleep(1)
	dev.device.touch(535,903,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(313,829,'DOWN_AND_UP')
	MonkeyRunner.sleep(3)
	dev.device.touch(202,531,'DOWN_AND_UP')
	MonkeyRunner.sleep(5)
	dev.device.touch(539,1800,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 11
	dev.device.touch(150,1788,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(551,627,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Call History'
	MonkeyRunner.sleep(1)
	dev.device.touch(535,903,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(627,1113,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(898,162,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 12
	dev.device.touch(150,1788,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(551,627,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Call History'
	MonkeyRunner.sleep(1)
	dev.device.touch(535,903,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(627,1113,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(1020,173,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(833,160,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(558,1385,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(1000,799,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Edit Number before Call'
	dev.device.touch(539,1800,'DOWN_AND_UP')
	MonkeyRunner.sleep(5)
	dev.device.touch(539,1800,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 13
	dev.device.touch(150,1788,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(551,627,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(720,177,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Call History'
	MonkeyRunner.sleep(1)
	dev.device.touch(1018,183,'DOWN_AND_UP')#menu
	MonkeyRunner.sleep(1)
	dev.device.touch(1018,183,'DOWN_AND_UP')#click delet
	MonkeyRunner.sleep(1)
	dev.device.touch(96,491,'DOWN_AND_UP')#choose the first history
	MonkeyRunner.sleep(1)
	dev.device.touch(927,170,'DOWN_AND_UP')#click delet pic
	MonkeyRunner.sleep(1)
	dev.device.touch(853,1158,'DOWN_AND_UP')#choose ok
	MonkeyRunner.sleep(1)
	print 'Delete Call Log'
	MonkeyRunner.sleep(2)

	#Case 14
	dev.device.touch(1018,183,'DOWN_AND_UP')#menu
	MonkeyRunner.sleep(1)
	dev.device.touch(739,305,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(853,1158,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Delete All Call Logs'
	MonkeyRunner.sleep(2)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 15
	dev.device.touch(150,1788,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(718,316,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(833,1235,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.press('KEYCODE_HOME','DOWN_AND_UP')
	MonkeyRunner.sleep(2)


#####################Browser######################
	print 'browser case'

	dev.device.touch(667,1800,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	#Case 1 & 2
	dev.device.touch(530,822,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Enter SOHU'
	MonkeyRunner.sleep(15)

	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(509,393,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Refresh'
	MonkeyRunner.sleep(15)

	#Case 3
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(509,393,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Refresh'
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(290,540,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Stop'
	MonkeyRunner.sleep(3)

	#Case 4
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(509,393,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Refresh'
	MonkeyRunner.sleep(15)
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(398,690,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Home Page'
	MonkeyRunner.sleep(3)

	#Case 5
	dev.device.touch(530,822,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Enter SOHU'
	MonkeyRunner.sleep(15)
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(397,815,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(753,319,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.type(str(Test_Count))
	MonkeyRunner.sleep(2)
	dev.device.touch(810,1187,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(898,1168,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Add Bookmark'
	MonkeyRunner.sleep(1)

	#Case 6
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(512,987,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(353,988,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Minimize'
	MonkeyRunner.sleep(1)
	dev.device.touch(667,1800,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Restore'
	MonkeyRunner.sleep(1)

	#Case 7
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(512,987,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(508,1133,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Closed'
	MonkeyRunner.sleep(3)

	#Case 8
	dev.device.touch(667,1800,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(530,822,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Enter SOHU'
	MonkeyRunner.sleep(15)
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(512,1121,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Saved Page'
	MonkeyRunner.sleep(2)

	#Case 9
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(533,1270,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(359,1828,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Shared via BT'
	MonkeyRunner.sleep(7)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 10
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(533,1270,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(526,1657,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Shared via Message'
	MonkeyRunner.sleep(5)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(890,1163,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	#Case 11
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(475,1377,'DOWN_AND_UP')#choose find on page
	MonkeyRunner.sleep(1)
	dev.device.touch(365,155,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.type('NBA')
	MonkeyRunner.sleep(1)
	print 'Search'
	MonkeyRunner.sleep(1)
	dev.device.touch(979,1817,'DOWN_AND_UP')#click ok
	MonkeyRunner.sleep(3)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	#Case 12
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(865,1562,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Request Desktop Version'
	MonkeyRunner.sleep(15)
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(865,1562,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Cancel'
	MonkeyRunner.sleep(15)

	#Case 13
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(611,1690,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Bookmarks/History'
	MonkeyRunner.sleep(3)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#Case 14
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(363,1847,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Settings'
	MonkeyRunner.sleep(2)
	dev.device.touch(333,319,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(980,725,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(266,457,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(951,792,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)


	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.press('KEYCODE_HOME','DOWN_AND_UP')
	MonkeyRunner.sleep(2)

#######################setting########################
	print 'setting case start'
	#case 1
	print 'case 1 setting the mobile data'
	print 'click setting on the desktop'
	dev.device.touch(408,1426,'DOWN_AND_UP')#click  the setting on the desktop
	MonkeyRunner.sleep(2)

	print 'click data useage'
	dev.device.touch(540,927,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'click mobile'
	dev.device.touch(810,327,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'click mobile data switch--->turn off the mobile data'
	dev.device.touch(962,493,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'agree turn off mobile data'
	dev.device.touch(887,1069,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'click mobile data switch--->turn on the mobile data'
	dev.device.touch(962,493,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'click the return button'
	dev.device.touch(84,159,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	print 'return the setting display'

	#case 2
	print 'case 2 setting light'
	print 'click display'
	dev.device.touch(540,1527,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'click brightness level'
	dev.device.touch(540,977,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'select the middle bright'
	dev.device.touch(540,213,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'select the mini bright'
	dev.device.touch(214,209,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'select the max bright'
	dev.device.touch(880,210,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(962,1194,'DOWN_AND_UP')

	#case 3
	print 'case 3 choose adaptive brightness'
	print 'click adaptive brightness switch'
	dev.device.touch(962,1194,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print('return the adaptive brigtness status')
	dev.device.touch(962,1194,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	#case 4
	print 'case 4 select sleep time'
	print 'click sleep'
	dev.device.touch(540,1438,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'choose sleep 30 minutes'
	dev.device.touch(540,1400,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'click the return button'
	dev.device.touch(84,159,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	print 'return the setting display'

	#case 5
	print 'case 5 choose general sound'
	print 'click sound&notification'
	dev.device.touch(540,1743,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'choose outdoor model'
	dev.device.touch(96,1028,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	#case 6
	print 'case 6: enter and set outdoor model vibrate'
	dev.device.touch(595,1040,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'swipe up the display'
	dev.device.drag((540,1524),(540,540),0.1)
	MonkeyRunner.sleep(2)

	print 'switch vibrate'
	dev.device.touch(540,1160,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'return the vibrate'
	dev.device.touch(540,1160,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	#case 7
	print 'case 7:switch touch sound'
	dev.device.touch(540,1502,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'return the touch sound'
	dev.device.touch(540,1502,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	#case 8
	print 'case 8:switch vibrate on touch'
	dev.device.touch(540,1840,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'return the vibrate on touch'
	dev.device.touch(540,1840,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#case 9
	MonkeyRunner.sleep(2)
	print 'case 9:swich standby intelligent power saving'
	print 'swipe up the setting display'
	dev.device.drag((540,1900),(540,0))
	MonkeyRunner.sleep(2)

	print 'click the battery button'
	dev.device.touch(540,479,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'switch power saving'
	dev.device.touch(540,323,'DOWN_AND_UP')#########(540,486)
	MonkeyRunner.sleep(2)

	print 'return power saving'
	dev.device.touch(540,323,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.press('KEYCODE_BACK','DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	#case 10
	print 'case 10:use pin to lock screen'
	dev.device.drag((540,1900),(540,0))
	MonkeyRunner.sleep(2)


	print 'click security'
	dev.device.touch(540,290,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'click screen lock'
	dev.device.touch(540,460,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'choose pin to lock screen'
	dev.device.touch(540,976,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'click continue'
	dev.device.touch(840,1833,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'enter 1234'
	dev.device.type('1234')
	MonkeyRunner.sleep(2)

	print 'click countinue'
	dev.device.touch(804,1165,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'confirm the pin 1234'
	dev.device.type('1234')
	MonkeyRunner.sleep(2)

	print 'click ok'
	dev.device.touch(804,1165,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'click setting done button'
	dev.device.touch(840,1833,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'click the power button'
	dev.device.press('KEYCODE_POWER','DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_POWER','DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.drag((540,1900),(540,0))
	MonkeyRunner.sleep(2)
	print 'enter 1234 to unlock the screen'
	dev.device.type('1234')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_DPAD_CENTER','DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'click screen lock'
	dev.device.touch(540,460,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'enter the pin'
	dev.device.type('1234')
	MonkeyRunner.sleep(2)

	print 'click continue'
	dev.device.touch(804,1165,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'click none to lock the screen'
	dev.device.touch(540,324,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'agree remove pin'
	dev.device.touch(873,1153,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.press('KEYCODE_BACK','DOWN_AND_UP')
	MonkeyRunner.sleep(2)


	#case 11
	print 'click Date&time'
	dev.device.touch(540,1268,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'click Automatic time zone'
	dev.device.touch(540,572,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'return Automatic time zone'
	dev.device.touch(540,572,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'click 24-hour format'
	dev.device.touch(540,1452,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	print 'return 24-hour format'
	dev.device.touch(540,1452,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.press('KEYCODE_BACK','DOWN_AND_UP')
	dev.device.press('KEYCODE_BACK','DOWN_AND_UP')
	print 'setting test finished'

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(3)


#######################contacts###################
	#Case 1
	dev.device.touch(396,1811,'DOWN_AND_UP')#destop
	MonkeyRunner.sleep(2)

	dev.device.touch(967,1823,'DOWN_AND_UP')#click add
	MonkeyRunner.sleep(1)
	dev.device.touch(585,331,'DOWN_AND_UP')#click usim
	MonkeyRunner.sleep(2)
	dev.device.touch(379,750,'DOWN_AND_UP')#choose the second phone contacts
	MonkeyRunner.sleep(2)

	print 'Add a Phone Contact'
	MonkeyRunner.sleep(2)
	dev.device.touch(518,522,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.type('AaBbCc'+ str(Test_Count))
	MonkeyRunner.sleep(2)
	dev.device.drag((838,1077),(838,306),1,10)
	MonkeyRunner.sleep(2)
	dev.device.touch(590,563,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.type('02165666666')
	MonkeyRunner.sleep(2)
	dev.device.touch(108,181,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.touch(967,1823,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(585,331,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(379,687,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	print 'Add a SIM card Contact'
	MonkeyRunner.sleep(1)
	dev.device.touch(398,567,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.type(str(Test_Count) +'zZyYxX')
	MonkeyRunner.sleep(2)
	dev.device.drag((788,1082),(788,330),1,10)
	MonkeyRunner.sleep(2)
	dev.device.touch(633,513,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.type('02165555555')
	MonkeyRunner.sleep(2)
	dev.device.touch(108,181,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.touch(866,160,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(393,158,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.type('aa')
	MonkeyRunner.sleep(1)
	dev.device.touch(993,1832,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	#Case 2&3
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(750,161,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(538,335,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(608,529,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Select Contacts'
	MonkeyRunner.sleep(1)
	dev.device.touch(876,163,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(823,1139,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Delete Selected Contacts'
	MonkeyRunner.sleep(1)

	#Case 5
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(715,447,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(608,1847,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(829,1850,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(98,348,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(880,159,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Import / Export Success'
	MonkeyRunner.sleep(2)


	#Case 6
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(715,447,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(1012,559,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(608,1847,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(829,1850,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(583,337,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(880,159,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Import / Export Success'
	MonkeyRunner.sleep(2)

	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(715,447,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(1012,559,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)

	dev.device.touch(608,1847,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(1020,561,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(793,1852,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(583,337,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(880,159,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(876,1157,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Import / Export Success'
	MonkeyRunner.sleep(2)



	#Case 8
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(770,590,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(1000,169,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(500,977,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'New SIM card Groups'
	MonkeyRunner.sleep(1)
	dev.device.touch(196,482,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.type('SIM' + str(Test_Count))
	MonkeyRunner.sleep(2)
	dev.device.touch(966,638,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(515,338,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(863,166,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(90,177,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(1000,169,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(576,1160,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'New phone Groups'
	MonkeyRunner.sleep(1)
	dev.device.touch(366,438,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.type('Phone' + str(Test_Count))
	MonkeyRunner.sleep(2)
	dev.device.touch(966,638,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(515,338,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(863,166,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(90,177,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	dev.device.touch(976,161,'DOWN_AND_UP')#click menu
	MonkeyRunner.sleep(2)
	dev.device.touch(753,333,'DOWN_AND_UP')#click delete
	MonkeyRunner.sleep(2)

	dev.device.touch(847,1124,'DOWN_AND_UP')#click ok
	MonkeyRunner.sleep(2)
	dev.device.touch(456,427,'DOWN_AND_UP')#enter group
	MonkeyRunner.sleep(2)
	dev.device.touch(976,161,'DOWN_AND_UP')#click menu
	MonkeyRunner.sleep(2)
	dev.device.touch(753,333,'DOWN_AND_UP')#click delete
	MonkeyRunner.sleep(2)
	dev.device.touch(847,1124,'DOWN_AND_UP')#click ok
	MonkeyRunner.sleep(2)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	# dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	# MonkeyRunner.sleep(2)

	# #Case 9
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(667,1040,'DOWN_AND_UP')#choose share
	MonkeyRunner.sleep(1)
	dev.device.touch(308,336,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(375,530,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(872,170,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(300,1480,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Contacts shared via Message'
	MonkeyRunner.sleep(5)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(866,1163,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	#Case 10
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(660,1040,'DOWN_AND_UP')#choose share
	MonkeyRunner.sleep(1)
	dev.device.touch(308,336,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(375,530,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(872,170,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(300,1666,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Contacts shared via MMS'
	MonkeyRunner.sleep(5)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(866,1163,'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	#Case 11
	dev.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(660,1040,'DOWN_AND_UP')#choose share
	MonkeyRunner.sleep(1)
	dev.device.touch(308,336,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(375,530,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(872,170,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.touch(286,1836,'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print 'Contacts shared via BT'
	MonkeyRunner.sleep(5)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)

	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_BACK', 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	dev.device.press('KEYCODE_HOME','DOWN_AND_UP')
	MonkeyRunner.sleep(2)

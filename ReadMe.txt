#coding = utf-8
预置条件
1.
2. Camera模块脚本放在文件管理器前面
3. 蓝牙默认为打开状态
4.流量开启状态
5.灭屏30钟
6.关闭横屏
7.锁频无
8.语言设置为英文
9.Clock修改为24小时制
10.开启手机模式
11.短信中有没有上海i生活信息（若无请申请，免费：联通发送短信SH到10655888009    ；电信发送短信SH到10625151009）
12.Contact第一次添加联系人选择USIM
13.手动添加联系人 10010
14.SMS设置中Notifications--off popup notification
15.设置快速拨号键2：10010
16.用过照相机
17.除了照相机以外的照片
18.使用一次讯飞输入法
19.输入法修改为google keypad
20.开启MTKlog
21.Batterylog点开菜单再退出即可
                           0. SMS脚本内手机号修改未当前测试号
                           0.在filemanager中新建CIT文件夹



****************
20151119:
1.更改了模块顺序，将garrly模块放在了file manager前面，camera后面，因为file manager 里面有一步是要删除所有dcmi的这个文件夹。在garrly中，是需要用到camera中的照片的
2.减少了一步battarylog这一步，因为在camera去删除所有照片只剩下一张的时候，会进入battary log 这个文件夹中。之后还会复制相册那个文件夹
3.增加了清除状态栏的代码

######
20151123
在图库删除照片的时候，因为坐标问题，仍需要开启BATTERLOG
但是图库仍在第五个。而不是第六个
#######
20151125
DCIM放在第五个，不新建CIT文件夹
filemanager的顺序：
Alarms
Android
assist
batterylog
DCIM
Download
iFlyIME
LOST.DIR
mtklog
Music
Padcasts
Recording
Ringtones



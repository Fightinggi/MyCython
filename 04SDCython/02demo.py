import win32gui
import win32con
import random

# 首先查找窗体，这里查找 qq。需要传入 窗口类名 窗口标题名，至于这个怎么获取可以使用 spy 工具查看
qq = win32gui.FindWindow("TXGuifoundation", "QQ")
# 然后让窗体显示出来
win32gui.ShowWindow(qq, win32con.SW_SHOW)
# 还可以隐藏
# win32gui.ShowWindow(qq, win32con.SW_HIDE)
# 主要要接收如下参数
# 参数一：控制的窗体
# 参数二：大致方位：HWND_TOPMOST，位于上方
# 参数三：位置x
# 参数四：位置y
# 参数五：长度
# 参数六：宽度
# 参数七：比较固定，就是让窗体一直显示
# win32gui.SetWindowPos(qq, win32con.HWND_TOPMOST, 100, 100, 300, 300, win32con.SWP_SHOWWINDOW)

# 将位置变成随机数
while True:
    x = random.randint(1, 1920)
    y = random.randint(1, 1080)
    win32gui.SetWindowPos(qq, win32con.HWND_TOPMOST, x, y, 300, 300, win32con.SWP_SHOWWINDOW)
print("Test Win API")
from ctypes import *

re = windll.user32.MessageBoxA(0, "窗口内容".encode("gbk"), "请选择".encode("gbk"), 1)  # 1 确认
if re == 1:
    windll.user32.MessageBoxW(0, "点击了确认按钮", "已选择", 0)
else:
    windll.user32.MessageBoxW(0, "点击了取消按钮", "已选择", 0)

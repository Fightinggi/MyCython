'''调用操作系统的库函数'''
from ctypes import *
import sys
import platform

# 判断当前的操作系统平台。
# Windows 平台返回 "Windows"，Linux 平台返回 "Linux"，MacOS 平台返回 "Darwin"
system = platform.system()

# 不同的平台共享库不同
if system == "Windows":
    lib = cdll.msvcrt
elif system == "Linux":
    lib = CDLL("libc.so.6")
elif system == "Darwin":
    lib = CDLL("libc.dylib")
else:
    print("不支持的平台，程序结束")
    sys.exit(0)

# 调用对应的函数，比如 printf，注意里面需要传入字节
lib.printf(b"my name is %s, age is %d\n", b"van", 37)  # my name is van, age is 37

# 如果包含汉字就不能使用 b"" 这种形式了，因为这种形式只适用于 ascii 字符，我们需要手动 encode 成 utf-8
lib.printf("姓名: %s, 年龄: %d\n".encode("utf-8"), "古明地觉".encode("utf-8"), 17)  # 姓名: 古明地觉, 年龄: 17

'''其他库函数'''
libc = cdll.msvcrt

# 创建一个大小为 10 的buffer
s = create_string_buffer(10)
# strcpy 表示将字符串进行拷贝
libc.strcpy(s, c_char_p(b"hello satori"))
# 由于 buffer 只有10个字节大小，所以无法完全拷贝
print(s.value)  # b'hello sato'


# 创建 unicode buffer
s = create_unicode_buffer(10)
libc.strcpy(s, c_wchar_p("我也觉得很变态啊"))
print(s.value)  # 我也觉得很变态啊

# 比如 puts 函数
libc.puts(b"hello world")  # hello world

'''其他库函数'''
# 我们通过 cdll.user32 本质上还是加载了 Windows 上的一个共享库
# 这个库给我们提供了很多方便的功能
win = cdll.user32

# 比如查看屏幕的分辨率
print(win.GetSystemMetrics(0))  # 1920
print(win.GetSystemMetrics(1))  # 1080

res = win.MessageBoxA(0,"窗口".encode("gbk"),"biaoti",1)
if res==1:
    print("sure")
else:
    print("OFF")
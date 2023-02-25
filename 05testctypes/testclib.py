# 直接调用平台中封装好的c语言dll库
print("Test C Lib")
from ctypes import *
from platform import system
sys = system()
print(sys)
if sys == "Windows":
    libc = cdll.msvcrt
elif sys == "Linux":
    libc = CDLL("libc.so.6")
elif sys == "Darwin":
    libc = CDLL("libc.dylib")
else:
    print("Unknow system")

libc.printf(b"Python string %s %d", b"str001", 1001)

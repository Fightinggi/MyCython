# 在c函数中调用python的函数callback
import ctypes
from ctypes import *

# 定义要被调用的函数callback
FUNC = CFUNCTYPE(None, c_int)


def call_back(a):
    print("py ", a)


callback = FUNC(call_back)

# 定义lib
dll_path = r"E:\VScodeProject\Ctypes\testctypes\x64\Debug\testctypes.dll"
lib = ctypes.CDLL(dll_path)

arr = [1, 2, 3, 4]
ArrType = c_int * len(arr)
carr = ArrType(*arr)

lib.TestCallback.restypes = (ArrType, c_int, FUNC)
lib.TestCallback(carr, len(arr), callback)

from ctypes import *
import ctypes.util


def find_dll(dll_name):
    return ctypes.util.find_library(dll_name)  # 查找dll


class StructionData(ctypes.Structure):
    _fields_ = [("hello", ctypes.c_void_p), ("printmsg", ctypes.c_void_p)]


def load_dll(dll_path):
    try:
        vc_dll = ctypes.CDLL(dll_path)  # 加载动态库，若失败抛出异常
        print("第一步，加载动态库成功")

        std = StructionData()

        print(std.hello)

        # vc_dll.test.restype = POINTER(StructionData)
        # p = vc_dll.test()
        # print(p.contents.name, p.contents.age)





    except OSError as e:
        print(e, "加载dll失败")


if __name__ == '__main__':
    # dll_path = find_dll("Dll1.dll")  # '.\\DemoDll.dll'
    dll_path = find_dll("test.dll")  # '.\\DemoDll.dll'
    if dll_path:
        load_dll(dll_path)

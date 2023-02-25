import ctypes.util
from ctypes import *


def find_dll(dll_name):
    return ctypes.util.find_library(dll_name)  # 查找dll


def load_dll(dll_path):
    try:
        vc_dll = ctypes.CDLL(dll_path)  # 加载动态库，若失败抛出异常
        print("第一步，加载动态库成功")

        vc_add = vc_dll.Add  # 取动态库的函数
        vc_TestCtypesNumber = vc_dll.TestCtypesNumber  # 取动态库的函数
        vc_TestStringA = vc_dll.TestStringA  # 取动态库的函数
        vc_TestStringW = vc_dll.TestStringW  # 取动态库的函数
        # vc_TestStringbuffer = vc_dll.TestStringbuffer  # 取动态库的函数

        vc_TestCtypesNumber.argtypes = [ctypes.c_int, ctypes.c_float, ctypes.c_int]  # 输入
        vc_TestStringA.argtypes = [ctypes.c_char_p, ctypes.c_int]  # 输入
        vc_TestStringW.argtypes = [ctypes.c_wchar_p, ctypes.c_int]  # 输入

        # vc_func.restypes = ctypes.c_int  # 返回值

        # str = b"vc_TestStringA"
        # print(vc_TestStringA(str, len(str)))
        #
        # str1 = "vc_TestStringW"
        # print(vc_TestStringW(str1, len(str1)))

        # 如果需要修改
        buf = create_string_buffer(b'aaaaa')
        vc_dll.TestStringbuffer(buf, 190)
        print("in python buf = ", repr(buf.raw), buf.value, len(buf), sep='\n')
        # in python buf =
        # b'@##aa\x00'                                 buf.raw
        # b'@##aa'                           buf.value
        # 10                                           len(buf)
        # TestStringbuffer : @#(1381177226)

        # 返回值
        print(vc_dll.TestReturnChar())  # 1788100608
        # 但我们希望的是获取地址指向的字符数组，所以我们需要指定一下返回的类型
        # 指定为 c_char_p，告诉 ctypes 你在解析的时候将 test1 的返回值按照 c_char_p 进行解析
        vc_dll.TestReturnChar.restype = c_char_p
        # 此时就没有问题了
        print(vc_dll.TestReturnChar())  # b'hello satori'

        # 同理对于 unicode 也是一样的，如果不指定类型，得到的依旧是一个整型
        vc_dll.TestReturnWChar.restype = c_wchar_p
        print(vc_dll.TestReturnWChar())  # 憨八嘎

        # 传递指针  指针的内容可以访问
        # ① python传到c中的指针的值 输入参数 可以被c修改再返回给python
        # ② 同理  c中定义的指针re  return 给 python ，python修改后，在调用函数 re值被改变
        vc_dll.TestPointer.argtypes = (POINTER(c_float),)
        vc_dll.TestPointer.restype = POINTER(c_void_p)
        f1 = c_float(88.8)
        # ① f1 在c中被修改  byref返回指针
        print("begin f1 = ", f1)  # begin f1 =  c_float(88.80000305175781)
        re = vc_dll.TestPointer(byref(f1))  # In C++ TestPointer re = 1001
        print("end f1 = ", f1)  # end f1 =  c_float(99.9000015258789)

        print("return re = ", re)  # return re =  <__main__.LP_c_void_p object at 0x00000297489B02C8>
        print("return re type = ", type(re))  # return re type =  <class '__main__.LP_c_void_p'>

        # ② re 在python中被修改  contents.value
        re.contents.value = 666
        print("In Python TestPointer re = ", re.contents.value)
        vc_dll.TestPointer(byref(f1))  # In C++ TestPointer re = 666

        # 传递数组
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # 定义数组类型 取名为TenArrType
        TenArrType = c_int * len(arr)
        # 初始化 TenArrType类对象 carr
        carr = TenArrType(*arr)  # 相当于TenArrType(1, 2, 3, 4, 5, 6, 7...)

        vc_dll.TestArray.argtypes = (TenArrType,)
        vc_dll.TestArray(carr, len(arr))

        # 传递结构体
        class Pos(Structure):
            _fields_ = [("x", c_int), ("y", c_int)]

        pos1 = Pos(11, 22)
        pos2 = Pos(33, 55)
        pos3 = [Pos(1, 1), Pos(2, 2), Pos(3, 3)]
        ThrPosType = Pos * len(pos3)
        cpos = ThrPosType(*pos3)

        vc_dll.TestStruct.argtypes = (Pos, POINTER(Pos), ThrPosType, c_int)  # 输入参数包装Pos

        # 返回结构体指针
        vc_dll.TestStruct.restype = POINTER(Pos)

        repos = vc_dll.TestStruct(pos1, byref(pos2), cpos, len(pos3))  # byref返回指针
        print("\nre x = y = \n", repos.contents.x, repos.contents.y)
        # 返回结构体对象
        vc_dll.GetPos.restype = Pos
        getpos = vc_dll.GetPos()
        print("返回结构体对象pos x = {},y = {}".format(getpos.x, getpos.y))




    except OSError as e:
        print(e, "加载dll失败")


if __name__ == '__main__':
    # dll_path = find_dll("testctypes.dll")  # '.\\DemoDll.dll'
    dll_path = find_dll(r"E:\VScodeProject\Ctypes\testctypes\x64\Debug\testctypes.dll")  # '.\\DemoDll.dll'
    if dll_path:
        load_dll(dll_path)

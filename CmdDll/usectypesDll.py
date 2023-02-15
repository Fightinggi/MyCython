import ctypes
import ctypes.util


def find_dll(dll_name):
    return ctypes.util.find_library(dll_name)  # 查找dll


def load_dll(dll_path):
    try:
        vc_dll = ctypes.CDLL(dll_path)  # 加载动态库，若失败抛出异常
        print("第一步，加载动态库成功")

        vc_func = vc_dll.add  # 取动态库的函数
        vc_func.argtypes = [ctypes.c_int, ctypes.c_int]  # 输入
        vc_func.restypes = ctypes.c_int  # 返回值

        ret = vc_func(1, 2)
        print("函数返回值：", ret)

        # my_list = [3, 21, 45, 6, 12]
        # array_len = len(my_list)
        #
        # # 把列表转换成c++动态库函数所需的参数数组
        # my_array = (ctypes.c_int * array_len)(*my_list)
        # ret = vc_func(my_array, array_len)
        #
        # print("函数返回值：", ret)
        #
        # my_array_newlist = []
        # for i in range(my_array._length_):
        #     my_array_newlist.append(my_array[i])
        #
        # print("新数组值：", my_array_newlist)

    except OSError as e:
        print(e, "加载dll失败")


if __name__ == '__main__':
    # dll_path = find_dll("Dll1.dll")  # '.\\DemoDll.dll'
    dll_path = find_dll("test.dll")  # '.\\DemoDll.dll'
    if dll_path:
        load_dll(dll_path)

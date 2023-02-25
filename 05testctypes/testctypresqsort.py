# 传递回调函数给c库函数qsort 进行快速排序  lib.qsort
from ctypes import *

lib = cdll.msvcrt  # 相对于 调用自己的dll库 lib = ctypes.CDLL(dll_path)
# _ACRTIMP void __cdecl qsort(
#     _Inout_updates_bytes_(_NumOfElements * _SizeOfElements) void*  _Base,
#     _In_                                                    size_t _NumOfElements,
#     _In_                                                    size_t _SizeOfElements,
#     _In_                _CoreCrtNonSecureSearchSortCompareFunction _CompareFunction
#     );
# CFUNCTYPE (restype, *argtypes,)  回调函数_CompareFunction 输入参数 (void const*, void const*)
CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))


def cmp_callback(a, b):
    # a是指向c_int
    return a.contents.value - b.contents.value


cmp_func = CMPFUNC(cmp_callback)
qsort = lib.qsort

# 排序的数据 整形列表
data = (c_int * 7)(1, 3, 4, 5, 65, 2, 12)
print(data)  # <__main__.c_long_Array_7 object at 0x000001FE149D9448>
print(*data)  # 1 3 4 5 65 2 12
for i in data:
    print(i, end=" ")
# void* _Base , size_t _NumOfElements,  size_t _SizeOfElements, _CompareFunction
qsort(data, len(data), sizeof(c_int), cmp_func)
for i in data:
    print(i, end=" ")

# extern关键词 调出.h文件 下的函数
cdef extern from "sub_core/sub.h":
    int sub(int a, int b)

# 然后用Cython重用包装调出来的函数sub
def sub_with_c(a, b):
    cdef int ret = sub(a,b)
    return ret
# 打印提交
import add

# 包装一个cython函数
print(add.add(2, 1))


# ext = Extension(name="wrapper_sub", sources=["sub.pyx", "sub_core/sub.c"], language_level=3)
# def sub_with_c(a, b):
#     return sub(a,b)
import wrapper_sub

print(wrapper_sub.sub_with_c(2, 1))

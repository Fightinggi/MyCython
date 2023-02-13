# from distutils.core import setup
#
# from Cython.Build import cythonize
#
# '''构建动态扩展库/模块'''
# # 1. 将Cython代码翻译成C代码  cythonize
# # 2. 根据C代码生成拓展模块  distutils.core.setup
# # 3. 终端输入 python .\setup.py build   生成build文件夹和add.c
# # 4. 将lib.win-amd64-cpython-39文件夹下的add.cp39-win_amd64.pyd文件放到setup同一目录下
# setup(ext_modules=cythonize("add.pyx", language_level=3))

from distutils.core import setup, Extension
from Cython.Build import cythonize
ext = Extension(name="wrapper_sub", sources=["sub.pyx", "sub_core/sub.c"], language_level=3)

setup(ext_modules=cythonize(ext))


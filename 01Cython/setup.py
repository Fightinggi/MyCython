'''调用add.pyx'''
from distutils.core import setup
from Cython.Build import cythonize

'''构建动态扩展库/模块'''
# 1. 将Cython代码翻译成C代码  cythonize
# 2. 根据C代码生成拓展模块  distutils.core.setup
# 3. 终端输入 python .\setup.py build   生成build文件夹和add.c
# 4. 将lib.win-amd64-cpython-39文件夹下的add.cp39-win_amd64.pyd文件放到setup同一目录下
setup(ext_modules=cythonize("add.pyx", language_level=3))

'''调用源文件和头文件'''
# from distutils.core import setup, Extension
# from Cython.Build import cythonize
# ext = Extension(name="wrapper_sub", sources=["sub.pyx", "sub_core/sub.c"], language_level=3)
#
# setup(ext_modules=cythonize(ext))

# '''实战  rxs_parsing_core'''
# import os
# import numpy
# from setuptools.command.build_ext import build_ext
# from setuptools.extension import Extension
# from setuptools import find_packages, setup
# from Cython.Build import cythonize
# def find_files(root, ext):
#     ret = list()
#     if os.path.exists(root):
#         for file in os.listdir(root):
#             if file.endswith(ext):
#                 ret.append(os.path.join(root, file))
#     return ret
#
# EXTENSIONS = []
#
# class Build(build_ext):
#     def build_extensions(self):
#         if self.compiler.compiler_type in ['unix', 'mingw32']:
#             for e in self.extensions:
#                 if e.name == "picoscenes":
#                     e.extra_compile_args = ['-std=c++2a', '-Wno-attributes',
#                                             '-O3']
#         if self.compiler.compiler_type in ["msvc"]:
#             for e in self.extensions:
#                 if e.name == "picoscenes":
#                     e.extra_compile_args = ['/std:c++latest']
#         super(Build, self).build_extensions()
#
# pico_root = "./rxs_parsing_core"
# pico_generated = os.path.join(pico_root, 'preprocess/generated')
# pico_include = os.path.join(pico_root, 'preprocess')
# pico_source = find_files(pico_root, '.cxx') + find_files(pico_generated, '.cpp')
# pico_extension = Extension(
#     "picoscenes", ["./picoscenes.pyx"] + pico_source,
#     include_dirs=[numpy.get_include(), pico_include],
#     define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
# )
# if os.path.exists(pico_root):
#     EXTENSIONS.append(pico_extension)
#
# setup(
#     packages=find_packages(),
#     install_requires=['numpy'],
#     python_requires='>=3',
#     ext_modules=cythonize(
#         EXTENSIONS,
#         compiler_directives={'language_level': 3, 'binding': False}
#     ),
#     cmdclass={'build_ext': Build},
# )






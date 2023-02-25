# python调用dll文件，在python执行文件.py 同一路径下，或者系统路径
from ctypes import *
irr = CDLL(r"E:\VScodeProject\CtypesAnLI\test_PyIrr\test_PyIrr\test_PyIrr.dll")
irr.InitDevice(800, 400)
# irr.LoadMap(br'E:\VScodeProject\CtypesAnLI\test_PyIrr\test_PyIrr\map-20kdm2.pk3', br'E:\VScodeProject\CtypesAnLI\test_PyIrr\test_PyIrr\maps\20kdm2.bsp')
irr.LoadMap(b'map-20kdm2.pk3', b'20kdm2.bsp')  # 把文件放在.py同一路径下，否则添加具体路径 如上

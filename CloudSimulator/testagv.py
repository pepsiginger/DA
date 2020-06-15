from ctypes import *
import ctypes


test = cdll.LoadLibrary("./performanceagv.so")

test.sim_cloud2.argtypes = (ctypes.c_int, ctypes.c_double)
test.sim_cloud2.restypes = ctypes.c_char

	
print(test.sim_cloud2(200,1))


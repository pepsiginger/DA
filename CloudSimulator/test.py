from ctypes import *
import ctypes
import sys

f = open("./data.txt",'w+')

test = cdll.LoadLibrary("./performancel.so")

test.sim_cloud2.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double)

#test.sim_cloud2(3,6000,100000,0.8,2)


for i in range(8):
	datarate = pow(2,i)
	print(test.sim_cloud2(3,6000,10000,datarate))	

#print(test.sim_cloud2(3,6000,100000,2))

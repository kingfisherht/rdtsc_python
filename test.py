from ctypes import *
lib = cdll.LoadLibrary('./DLL3.dll')
lib.get_rdtsc.restype = c_longlong
data = lib.get_rdtsc()

print(data)

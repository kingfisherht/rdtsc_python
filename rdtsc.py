from ctypes import *
from ctypes import c_longlong
import sys
try:  
    lib = cdll.LoadLibrary('./rdtsc.so')  
except:  
    print("error for load lib")
    exit
target = c_longlong(lib.get_rdtsc())

print ("%Ld"%target)

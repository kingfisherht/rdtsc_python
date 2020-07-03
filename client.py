from ctypes import *
import sys
try:  
    lib = cdll.LoadLibrary('./rdtsc.so')  
except:  
    print("error for load lib")
    exit
target = lib.get_rdtsc()
print ("0x%x"%target)

import socket
import numpy as np
from ctypes import *
from ctypes import c_longlong as ll
import time
BUFSIZE = 1024
try:  
    lib = cdll.LoadLibrary('./rdtsc.so')  
except:  
    print("error for load lib")
    exit
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 9999)
data = []
for i in range(1,100):
    data.append(i)
while True:
    lib.get_rdtsc.restype = c_longlong
    target = lib.get_rdtsc()
    print(target)
    data.append(target)
    msg = str(data)
    client.sendto(msg.encode(),ip_port)
    data.pop()
    time.sleep(1)
client.close()
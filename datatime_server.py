import socket
from ctypes import *
try:  
    lib = cdll.LoadLibrary('./rdtsc.so')  
except:  
    print("error for load lib")
    exit
BUFSIZE = 1024
ip_port = ('0.0.0.0', 9999)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ip_port)
while True:
    msg,client= server.recvfrom(BUFSIZE)
    lib.get_rdtsc.restype = c_longlong
    end = lib.get_rdtsc()
    data = int (msg.decode().split(" ")[-1].split("]")[0])
    print(data)
    diff = end - data
    print(diff)
server.close()
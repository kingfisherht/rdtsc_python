import socket
import sys
from ctypes import *
import time 

HOST, PORT = "localhost", 9999
data = "hello world"
lib = cdll.LoadLibrary('./rdtsc.so')
lib.get_rdtsc.restype = c_longlong 
# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
while True:
    start = lib.get_rdtsc()
    sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")
    end =  lib.get_rdtsc()
    print (end-start)
    time.sleep(1)
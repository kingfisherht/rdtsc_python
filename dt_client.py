import socket
import datetime
import numpy as np
from ctypes import *
from ctypes import c_longlong as ll
import time
BUFSIZE = 1024
data = []
for i in range(1,100):
    data.append(i)
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 9999)
while True:
    time_t = datetime.datetime.now()
    print (time_t)
    data.append(time_t)
    msg = str(data)
    client.sendto(msg.encode(),ip_port)
    data.pop()
    time.sleep(1)
client.close()
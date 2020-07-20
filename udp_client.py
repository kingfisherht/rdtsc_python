import socket
import sys
from ctypes import *
import time 
count = 0
count_t4 = 0 
count_t8 = 0
count_t16 = 0
count_t32 = 0
count_t64 = 0 
count_t128 = 0
count_t256 = 0
max_latency = 0
HOST, PORT = "10.67.106.190", 9999
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
    diff_time  = (end -start)/2112000.0
    if diff_time > max_latency:
        max_latency = diff_time

    if diff_time < 4 :
        count_t4 += 1
    elif diff_time >=4 and diff_time < 8:
        count_t8 += 1
    elif diff_time >=8 and diff_time < 16:
        count_t16 +=1
    elif diff_time >=16 and diff_time < 32:
        count_t32 +=1
    elif diff_time >=32 and diff_time < 64:
        count_t64 +=1
    elif diff_time >=64 and diff_time < 128:
        count_t128 +=1
    elif diff_time >=128 and diff_time < 256:
        count_t256 +=1
    else:
        count +=1

   # print ("\r"+"max latency : {:0.3f}ms".format(max_latency),end = "",flush=True)
    #print ("\r"+"UDP | 0ms~4ms | 4ms~8ms |8ms~16ms |16ms~32ms | 32ms~64ms | 64ms~128ms | 64ms~128ms | 128ms~256ms | > 256ms |",end = "",flush=True)
    print("\r"+"CONT|   {0}     |   {1}     |   {2}     |   {3}      |   {4}       |    {5}       |    {6}       |        {7}    |".format(
        count_t4,count_t8,count_t16,count_t32,count_t64,count_t128,count_t256,count
    ),end = "",flush=True)

    time.sleep(0.1)
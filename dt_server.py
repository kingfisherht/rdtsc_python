import socket
import datetime
from ctypes import *
BUFSIZE = 1024
ip_port = ('0.0.0.0', 9999)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ip_port)
while True:
    msg,client= server.recvfrom(BUFSIZE)
    native_time = datetime.datetime.now().microsecond
    #print ("native",native_time)
    data = int (msg.decode().split(" ")[-1].split(")")[0])
    #print ("revice",data)
    print("diff:",native_time-data)
    


server.close()
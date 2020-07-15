# encoding: UTF-8
import threading
from datetime import datetime
import time

def func():
     print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

timer = threading.Timer(1, func)
timer.start()
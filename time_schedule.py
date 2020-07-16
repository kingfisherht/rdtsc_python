import schedule
import time
from datetime import datetime
from time import time
start_ms = 0
start_s = 0
 
def print_time():
    global start_ms, start_s
    expect_ms = start_ms + 4000
    expect_s = start_s
    if(expect_ms > 1000000):
        expect_ms -= 1000000
        expect_s += 1
    data_now = datetime.now()
    data_s = int(time.mktime(data_now.timetuple()))
    data_ms = data_now.microsecond
    s_diff = data_s - expect_s
    ms_diff = data_ms - expect_ms
    print("data_ms:",data_ms)
    print("expect_ms:",expect_ms)
    print("data_s:",data_s)
    print("expect_s:",expect_s)
    print("s_diff:",s_diff)
    print("ms_diff:",ms_diff)
    print("latency: ",s_diff*1000000 + ms_diff)
    print(" ")
    start_ms = expect_ms
    start_s = expect_s
 

if __name__ == "__main__":
    start_time = datetime.now()
    print("+++_____", time()*1000)
    print(start_time)
    print()
    start_ms = start_time.microsecond
    start_s = int(time.mktime(start_time.timetuple()))
    schedule.every(0.004).seconds.do(print_time)
    while True:
       schedule.run_pending()


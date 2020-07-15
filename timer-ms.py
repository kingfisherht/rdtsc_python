import sched
import time
from datetime import datetime
schedule = sched.scheduler(time.time, time.sleep)

def timetostamp(stamp):
    timeStamp = float(stamp/1000000) 
    timeArray = time.localtime(timeStamp) 
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    #print(otherStyleTime)

def printTime(inc,start_ms,start_s):
    expect = start_ms + 4
    #timetostamp(start)
    data_now = datetime.now()
    data_s = int(time.mktime(data_now.timetuple()))
    data_ms = data_now.microsecond
    s_diff = data_s - start_s
    ms_diff = data_ms - expect
    print("data_ms:",data_ms)
    print("expect:",expect)
    print("s_diff:",s_diff)
    print("ms_diff:",ms_diff)
    print(" ")
    schedule.enter(inc, 0, printTime, (inc,expect,start_s))

if __name__ == "__main__":
    start_time = datetime.now()
    start_ms = start_time.microsecond
    start_s = int(time.mktime(start_time.timetuple()))
    schedule.enter(0, 0, printTime, (0.04,start_ms,start_s))
    schedule.run()

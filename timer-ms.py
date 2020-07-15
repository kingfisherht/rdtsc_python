import sched
import time
from datetime import datetime
schedule = sched.scheduler(time.time, time.sleep)

def timetostamp(stamp):
    timeStamp = float(stamp/1000) 
    timeArray = time.localtime(timeStamp) 
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)

def printTime(inc,start):
    expect = start + 4
    timetostamp(start)
    data = datetime.now()
    print ("data:",data)
    diff = int(time.mktime(data.timetuple()) * 1000.0 + data.microsecond / 1000.0) - expect
    #print(diff)
    schedule.enter(inc, 0, printTime, (inc,expect))

def begin_time(inc,start):
    schedule.enter(0, 0, printTime, (inc,start))
    schedule.run()

if __name__ == "__main__":
    start = datetime.now()
    start_ms = int(time.mktime(start.timetuple()) * 1000.0 + start.microsecond / 1000.0)
    begin_time(0.04,start_ms)

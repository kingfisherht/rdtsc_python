import schedule
import time
from datetime import datetime
now = 0
next_time = 0
expect = 0
def job():
    global now,next_time
    now = time.time()*1000000
    expect = next_time + 1000000
    print (now-expect)
    next_time = expect


next_time = time.time()*1000000
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()

import sched
import time
from datetime import datetime
schedule = sched.scheduler(time.time, time.sleep)
def printTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    schedule.enter(inc, 0, printTime, (inc,))

def main(inc=60):
    schedule.enter(0, 0, printTime, (inc,))
    schedule.run()

main(1)

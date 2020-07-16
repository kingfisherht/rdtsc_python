import schedule
import time
from datetime import datetime
 
def print_time():
    print(datetime.now())

schedule.every(0.004).seconds.do(print_time)
 
while True:
    schedule.run_pending()


import time
from datetime import datetime
def stamptotime(stamp):
    timeStamp = float(stamp/1000) 
    timeArray = time.localtime(timeStamp) 
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S.%f", timeArray)
    print(otherStyleTime)

def timetoStamp(timestr):
    datetime_obj = datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S.%f")
    obj_stamp = int(time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0)
    print(obj_stamp)
    return obj_stamp

if __name__ == "__main__":
    data = datetime.now()
    print("data:",data)
    stampd = timetoStamp(str(data))
    stamptotime(stampd)


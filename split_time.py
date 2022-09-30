import sys
import datetime


def convert_24(time):
    if time[-2:] == 'AM' and time[0:2] == '12':
        return '00' + time[2:-2]
    elif time[-2:] == 'AM':
        return time[:-2]
    elif time[-2:] == 'PM' and time[0:2] == '12':
        return time[:-2]
    else:
        return str(int(time[0:2])+12) + time[2:8]


def assign_interval(time):
    hr, min, sec = time.split(':')
    t1 = datetime.time(int(hr), int(min), int(sec))
    # create interval
    interval_start_1 = datetime.time(0, 0, 0)
    interval_end_1 = datetime.time(3, 59, 59)

    interval_start_2 = datetime.time(4, 0, 0)
    interval_end_2 = datetime.time(7, 59, 59)

    interval_start_3 = datetime.time(8, 0, 0)
    interval_end_3 = datetime.time(11, 59, 59)

    interval_start_4 = datetime.time(12, 0, 0)
    interval_end_4 = datetime.time(15, 59, 59)

    interval_start_5 = datetime.time(16, 0, 0)
    interval_end_5 = datetime.time(19, 59, 59)

    if interval_start_1 <= t1 <= interval_end_1:
        return 1
    elif interval_start_2 <= t1 <= interval_end_2:
        return 2
    elif interval_start_3 <= t1 <= interval_end_3:
        return 3
    elif interval_start_4 <= t1 <= interval_end_4:
        return 4
    elif interval_start_5 <= t1 <= interval_end_5:
        return 5
    else:
        return 6


def split_time(time):
    hr = time[0:2]
    min = time[2:4]
    period = time[4:]
    period = 'AM' if period == 'A' else 'PM'
    time = hr+':'+min+':'+'00'+period
    time = convert_24(time)
    return time


for line in sys.stdin:
    line = line.strip("\n\r")
    time, violation_code = line.split("\t")
    time = split_time(time)
    interval = assign_interval(time)
    result = '\t'.join([time, violation_code, str(interval)])
    print(result)

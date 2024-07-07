#!/usr/bin/env python3

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    '''convert a given number of seconds to a time object in hour, minute, second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    seconds1 = time_to_sec(t1)
    seconds2 = time_to_sec(t2)
    total_seconds = seconds1 + seconds2
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    total_seconds = time_to_sec(time) + seconds
    if total_seconds < 0:
        total_seconds = 0
    updated_time = sec_to_time(total_seconds)
    time.hour = updated_time.hour
    time.minute = updated_time.minute
    time.second = updated_time.second
    return None

def format_time(t):
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

# This is just a helper function, not part of the original instructions
def print_time(t):
    print(f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}')

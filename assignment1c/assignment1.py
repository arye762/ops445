#!/usr/bin/env python3

"""
OPS445 Assignment 1 - Fall 2023
Program: assignment1.py
The python code in this file is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Arie Cimafranca
Description: This program calculates the end date from a specified start
date and a number of days which can be positive (future) or negative (past).
It handles different year lengths, leap years, and varying month lengths,
ensuring accurate date calculations. The program outputs the final date with
the corresponding day of the week.
"""

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    if month == 2:
        return 29 if leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def after(date: str) -> str:
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day

    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap year

    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict[mon]

    if day > mon_max:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    day, month, year = (int(x) for x in date.split('/'))

    # Handling the first day of the month
    if day == 1:
        # If January 1st, roll back to December 31st of the previous year
        if month == 1:
            return f'31/12/{year - 1}'
        else:
            # Check the number of days in the previous month
            previous_month = month - 1
            previous_month_days = mon_max(previous_month, year)
            return f'{previous_month_days}/{previous_month:02}/{year}'
    else:
        # Not the first day of the month, simply decrement the day
        return f'{day - 1:02}/{month:02}/{year}'

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    try:
        day, month, year = map(int, date.split('/'))
        print(f"Debug: Parsed date - Day: {day}, Month: {month}, Year: {year}")

        if year < 1583:
            print("Debug: Year is less than 1583.")
            return False
        if month < 1 or month > 12:
            print(f"Debug: Month {month} is outside 1-12 range.")
            return False
        if day < 1 or day > mon_max(month, year):
            print(f"Debug: Day {day} is outside 1-{mon_max(month, year)} range for month {month}, year {year}.")
            return False

        print("Debug: Date is valid.")
        return True

    except ValueError as e:
        print(f"Error parsing date: {e}")
        return False


def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"
    current_date = start_date
    if num >= 0:
        for _ in range(num):
            current_date = after(current_date)
    else:
        for _ in range(-num):
            current_date = before(current_date)
    return current_date


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    start_date, num_days = sys.argv[1], sys.argv[2]

    if not valid_date(start_date) or not num_days.lstrip('-').isdigit():
        usage()

    num_days = int(num_days)
    end_date = day_iter(start_date, num_days)
    day_name = day_of_week(end_date)
    print(f'The end date is {day_name}, {end_date}.')

if __name__ == "__main__":
    # check length of arguments
    # check first arg is a valid date
    # check that second arg is a valid number (+/-)
    # call day_iter function to get end date, save to x
    # print(f'The end date is {day_of_week(x)}, {x}.')
    pass
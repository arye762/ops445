#!/usr/bin/env python3

# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    return s[:5]

def last_seven(s):
    return s[-7:]

def middle_number(n):
    s = str(n)
    return s[1:3]

def first_three_last_three(s1, s2):
    return s1[:3] + s2[-3:]

if __name__ == '__main__':
    print(first_five(str1))      # Expected output: 'Hello'
    print(first_five(str2))      # Expected output: 'Senec'
    print(last_seven(str1))      # Expected output: 'World!!'
    print(last_seven(str2))      # Expected output: 'College'
    print(middle_number(num1))   # Expected output: '50'
    print(middle_number(num2))   # Expected output: '.5'
    print(first_three_last_three(str1, str2))  # Expected output: 'Helege'
    print(first_three_last_three(str2, str1))  # Expected output: 'Send!!'

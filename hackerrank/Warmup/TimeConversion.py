'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. 
Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Output Format

Convert and print the given time in 24-hour format, where 00 <= hh <= 23.

link: https://www.hackerrank.com/challenges/time-conversion/problem
'''
import sys

def timeConversion(s):
    zn = s[-2:]
    if zn == "PM" and s[:2] != "12":
        s = str(12 + int(s[:2])) + s[2:]
    if zn == "AM" and s[:2] == "12":
        s = "00" + s[2:]
    return s[:-2]

s = raw_input().strip()
result = timeConversion(s)
print(result)
'''
find the 256th day of a given year.

link: https://www.hackerrank.com/challenges/day-of-the-programmer/problem

'''
import sys
thirty = [1, 3, 6, 7, 8]
def leap_year(year):
    if year < 1919:
        return year % 4 == 0
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0
    
def solve(year):    
    days = 0
    for i in range(1, 9):
        if i != 2 and i in thirty:
            days += 31
        elif i == 2:
            if year == 1918 and leap_year(year):
                days += (29-13)
            elif year == 1918 and not leap_year(year):
                days += (28 - 13)
            elif leap_year(year):
                days += 29
            else:
                days += 28
        else:
            days += 30
    
    d = 256 - days
    return "%d.%02d.%d" % (d, 9, year)

year = int(raw_input().strip())
result = solve(year)
print(result)
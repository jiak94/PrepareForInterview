'''
At HackerLand University, a passing grade is any grade 40 points or higher
a 100 point scale. Sam is a professor at the university and likes to round 
each student’s grade according to the following rules:

If the difference between the grade and the next higher multiple of 5 is 
less than 3, round to the next higher multiple of 5

If the grade is less than 38, don’t bother as it’s still a failing grade

Automate the rounding process then round a list of grades and print the 
results.

Output Format

For each grade_i of the n grades, print the rounded grade on a new line.

link: https://www.hackerrank.com/challenges/grading/problem
'''
import sys

def solve(grades):
    res = list()
    # Complete this function
    for g in grades:
        if g < 38:
            res.append(g)
        else:
            five_count = int(g/5)
            next_five = (five_count+1)*5
            if next_five - g < 3:
                res.append(next_five)
            else:
                res.append(g)
    return res
n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
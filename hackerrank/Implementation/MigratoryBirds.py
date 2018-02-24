'''
return the id of max occurance

Output Format
Print the type number of the most common bird;
if two or more types of birds are equally common, 
choose the type with the smallest ID number.

link: https://www.hackerrank.com/challenges/migratory-birds/problem
'''
import sys

def migratoryBirds(n, ar):
    count = dict()
    for bird in ar:
        if bird in count:
            count[bird] += 1
        else:
            count[bird] = 1
    return max(count, key=count.get)

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)
'''
Calculate and print the sum of the elements in an array, 
keeping in mind that some of those integers may be quite large.

Output:
Print the integer sum of the elements in the array.

link: https://www.hackerrank.com/challenges/a-very-big-sum/problem
'''

def aVeryBigSum(n, ar):
    res = 0
    for n in ar:
        res += n
    return res
    
n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)
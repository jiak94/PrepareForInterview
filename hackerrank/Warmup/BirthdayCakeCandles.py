'''
Colleen is having a birthday! She will have a cake with one candle for 
each year of her age. When she blows out the candles, she’ll only be able 
to blow out the tallest ones.

Find and print the number of candles she can successfully blow out.

Output Format 
Print the number of candles the can be blown out on a new line.

link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
'''
import sys

def birthdayCakeCandles(n, ar):
    return ar.count(max(ar))

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
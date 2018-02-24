'''
Sam's house has an apple tree and an orange tree that yield an 
abundance of fruit. Sam’s two children, Larry and Rob, decide to play 
a game in which they each climb a tree and throw fruit at their (Sam’s) 
house. Each fruit that lands on the house scores one point for the one 
who threw it. Larry climbs the tree on the left (the apple), and Rob 
climbs the one on the right (the orange).

Print two lines of output:

On the first line, print the number of apples that fall on Sam's house.
On the second line, print the number of oranges that fall on Sam's house.

link: https://www.hackerrank.com/challenges/apple-and-orange/problem
'''
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Complete this function
    res = list()
    apple_score = 0
    oranges_score = 0
    for apple in apples:
        if apple + a >= s and apple + a <=t:
            apple_score += 1
    print apple_score
    for orange in oranges:
        if b + orange >= s and b + orange <= t:
            oranges_score += 1
    print oranges_score
    return [apple_score, oranges_score]

if __name__ == "__main__":
    s, t = raw_input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = raw_input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = raw_input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = map(int, raw_input().strip().split(' '))
    orange = map(int, raw_input().strip().split(' '))
    countApplesAndOranges(s, t, a, b, apple, orange)
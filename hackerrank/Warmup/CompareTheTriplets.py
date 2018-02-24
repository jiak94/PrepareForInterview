'''
Alice and Bob each created one problem for HackerRank. 
A reviewer rates the two challenges, awarding points on a scale from 
1 to 100 for three categories: problem clarity, originality, 
and difficulty.

We define the rating for Alice's challenge to be the triplet
A = (a0, a1, a2) and the rating for Bob's challenge to be the triplet 
B = (b0, b1, b2)

Your task is to find their comparison points by comparing a0
with b0, a1 with b1, and a2 with b2.

if a_i > b_i, then Alice is awarded 1 point
if a_i < b_i, then Bob is awarded 1 point
if a_i == b_i, then neither person receives a point

Output Format

Print two space-separated integers denoting the respective comparison 
points earned by Alice and Bob.

link: https://www.hackerrank.com/challenges/compare-the-triplets/problem
'''
import sys

def solve(a0, a1, a2, b0, b1, b2):
    a_score = 0
    b_score = 0
    if (a0 < b0):
        b_score += 1
    if (a1 < b1):
        b_score += 1
    if (a2 < b2):
        b_score += 1
    
    if (a0 > b0):
        a_score += 1
    if (a1 > b1):
        a_score += 1
    if (a2 > b2):
        a_score += 1
    
    return [a_score, b_score]

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
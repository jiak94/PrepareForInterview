'''
Maria plays  games of college basketball in a season. 
Because she wants to go pro, she tracks her points scored per 
game sequentially in an array defined as score. After each game, 
she checks to see if score  breaks her record for most or 
least points scored so far during that season.

Output Format

Print two space-seperated integers describing the respective 
numbers of times her best (highest) score increased and her 
worst (lowest) score decreased.

link: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
'''
import sys

def breakingRecords(score):
    best_inc = 0
    worst_dec = 0
    max_score = score[0]
    min_score = score[0]
    for i in range(1, len(score)):
        if score[i] > max_score:
            best_inc += 1
            max_score = score[i]
        if score[i] < min_score:
            worst_dec += 1
            min_score = score[i]
    return [best_inc, worst_dec]
    

if __name__ == "__main__":
    n = int(raw_input().strip())
    score = map(int, raw_input().strip().split(' '))
    result = breakingRecords(score)
    print " ".join(map(str, result))
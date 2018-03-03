'''
Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

Its length is at least .
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

link: https://www.hackerrank.com/challenges/strong-password/problem
'''
import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def minimumNumber(n, password):
    num = 0
    upper = 0
    lower = 0
    special = 0
    
    for char in password:
        if char in numbers:
            num = 1
        elif char in lower_case:
            lower = 1
        elif char in upper_case:
            upper = 1
        elif char in special_characters:
            special = 1
    arr = [num, upper, lower, special]
    count = arr.count(0)
    if n < 6:
        if 6 - n < count:
            return count
        else:
            return 6 - n
    return count
            
            

if __name__ == "__main__":
    n = int(raw_input().strip())
    password = raw_input().strip()
    answer = minimumNumber(n, password)
    print answer
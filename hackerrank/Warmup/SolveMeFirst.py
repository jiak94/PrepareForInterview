'''
int solveMeFirst(int x, int y);
x is the first integer input
y is the second integer input

return: sum of above two integers

link:
https://www.hackerrank.com/challenges/solve-me-first/problem
'''

def solveMeFirst(a, b):
    return a + b

if __name__ == "__main__":
    num1 = input()
    num2 = input()
    res = solveMeFirst(num1, num2)
    print(res)
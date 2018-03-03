'''
Caesar Cipher
link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem
'''
import sys

def caesarCipher(s, k):
    output = list(s)
    k %= (ord('z') - ord('a') + 1)
     
    for idx, l in enumerate(output):
        if l.isalpha():
            if l.isupper():
                new_char = ord(l)+k
                if new_char > ord('Z'):
                    new_char = new_char - ord('Z') + ord('A') - 1
                output[idx] = chr(new_char)
            else:
                new_char = ord(l)+k
                if new_char > ord('z'):
                    new_char = new_char - ord('z') + ord('a') - 1
                output[idx] = chr(new_char)
    return ''.join(output)
            

if __name__ == "__main__":
    n = int(raw_input().strip())
    s = raw_input().strip()
    k = int(raw_input().strip())
    result = caesarCipher(s, k)
    print result
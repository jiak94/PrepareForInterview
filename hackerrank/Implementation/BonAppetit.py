'''
Anna and Brian order  items at a restaurant, but Anna declines to eat any of the  item (where ) due to an allergy. When the check comes, they decide to split the cost of all the items they shared; however, Brian may have forgotten that they didn't split the  item and accidentally charged Anna for it.

link: https://www.hackerrank.com/challenges/bon-appetit/problem
'''
n, k = map(int, raw_input().split())
arr = map(int, raw_input().split())
val = input()
t = val - (sum(arr) - arr[k])/2
if (t == 0):
    print "Bon Appetit"
else:
    assert val == sum(arr)/2
    print t
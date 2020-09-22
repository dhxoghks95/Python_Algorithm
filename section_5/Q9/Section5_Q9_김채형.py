"""
Section 5 - Q9

아나그램
"""

import sys
sys.stdin = open('input.txt', 'r')
a = input()
b = input()
dic_a = dict()
dic_b = dict()
for alpha in a:
    dic_a[alpha] = dic_a.get(alpha, 0)+1
for alpha in b:
    dic_b[alpha] = dic_b.get(alpha, 0)+1
#print(dic_a)
#print(dic_b)

for key in dic_a.keys():
    if key in dic_b.keys(): # key는 같은데
        if dic_a[key]!=dic_b[key]: # value가 다르면
            print('NO')
            break
    else: # key 자체가 달라버리면
        print('NO')
        break

else:
    print('YES')

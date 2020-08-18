"""
Section 3 - Q3

카드 역배치(정올 기출)
"""

import sys
sys.stdin = open('input.txt', 'r')

seq = list(range(1, 21))

for i in range(10):
    start, end = map(int, input().split(' '))
    subset = seq[start-1:end]
    #print(subset)

    subset_reversed = []
    for j in range(len(subset)):
        subset_reversed.append(subset[len(subset)-1-j])
    #print(subset_reversed)

    for k in range(start-1, end):
        seq[k] = subset_reversed[k-start+1]

    #print(seq)

print(seq)

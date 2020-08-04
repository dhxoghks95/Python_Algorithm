import sys
from collections import Counter
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
tmp = []

for i in range(n):
    for j in range(m):
        tmp.append(i+j+2)

answer = []
tmp2 = Counter(tmp).most_common(m-n+1)
for idx in range(len(tmp2)):
    answer.append(tmp2[idx][0])

print(*answer)

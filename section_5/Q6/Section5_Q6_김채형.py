"""
Section 5 - Q6

응급실
"""

import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split(' '))
ls = list(map(int, input().split(' ')))
que = deque()
for idx, ele in enumerate(ls):
    que.append((idx, ele))
print(que)

cnt = 0 # 진료 횟수
while que:
    now = que.popleft()
    if any(now[1]<x[1] for x in que):
        que.append(now)
    else:
        cnt += 1
        if now[0]==m:
            print(cnt)
            break

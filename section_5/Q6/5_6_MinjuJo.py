import sys
from collections import deque
sys.stdin = open("in5.txt", "r")

num, order = map(int, input().split())
danger = list(map(int, input().split()))
chart = deque()

for i, dan in enumerate(danger):
    chart.append((i, dan))

hi = 0
while True:
    new = chart.popleft()
    if max(danger) == new[1]:
        hi += 1
        if order == new[0]:
            print(hi)
            break
        else:
            danger.remove(max(danger))
    else:
        chart.append(new)
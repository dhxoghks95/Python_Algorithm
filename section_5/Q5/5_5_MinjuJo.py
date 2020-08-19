import sys
from collections import deque

sys.stdin = open("in5.txt", "r")
prince, num = map(int, input().split())

queue = deque(list(range(1, prince + 1)))

while len(queue) > 1:
    queue.rotate(-num)
    queue.pop()

last = queue.pop()
print(last)
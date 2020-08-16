import sys

sys.stdin = open("./input8.txt", "r")
n = int(input())
s1 = set()
s2 = set()

for _ in range(n):
    s1.add(input())

for _ in range(n-1):
    s2.add(input())

print(*s1 - s2)

import sys

sys.stdin = open("./input7.txt", 'r')
N = int(input())
coins = [int(x) for x in input().split()]
M = int(input())
cnt = 0

for coin in reversed(coins):
    if M == 0:
        break
    q = M // coin
    M -= coin * q
    cnt += q

print(cnt)

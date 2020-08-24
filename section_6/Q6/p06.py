import sys

sys.stdin = open("./input6.txt", 'r')

N, M = list(map(int, input().split()))
s = list(range(1, N+1))


def permute(new_s):
    if len(new_s) == M:
        print(*new_s)
        return
    else:
        for idx in range(len(s)):
            new_s.append(s[idx])
            permute(new_s)
            new_s.pop()


permute([])

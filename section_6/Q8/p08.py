import sys

sys.stdin = open("./input8.txt", 'r')

N, M = list(map(int, input().split()))
s = list(range(1, N+1))


def permute(new_s):
    if len(new_s) == M:
        print(*new_s)
        return
    else:
        for i in range(len(s)):
            if s[i] not in new_s:
                new_s.append(s[i])
                permute(new_s)
                new_s.pop()


permute([])

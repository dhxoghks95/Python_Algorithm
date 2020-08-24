import sys

sys.stdin = open("./input11.txt", 'r')

N, K = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]
M = int(input())
cnt = 0


def permute(idx, new_s):
    global cnt
    if len(new_s) == K:
        if sum(new_s) % M == 0:
            cnt += 1
        return
    else:
        for i in range(idx+1, len(s)):
            new_s.append(s[i])
            permute(i, new_s)
            new_s.pop()


permute(-1, [])
print(cnt)

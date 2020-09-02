import sys

sys.stdin = open("./input10.txt", 'r')

N, M = list(map(int, input().split()))
s = list(range(1, N+1))
cnt = 0


def permute(idx, new_s):
    global cnt
    if len(new_s) == M:
        cnt += 1
        print(*new_s)
        return
    else:
        for i in range(idx, len(s)):
            new_s.append(s[i])
            permute(i+1, new_s)
            new_s.pop()


permute(0, [])
print(cnt)

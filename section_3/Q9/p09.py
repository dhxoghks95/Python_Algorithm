N = int(input())

lst = [[0] * (N+2)]
for _ in range(N):
    lst.append([0] + list(map(int, input().split())) + [0])
lst.append([0] * (N+2))


res = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        tmp = lst[i][j]
        res += 1 if (tmp > lst[i][j-1] and tmp > lst[i][j+1] and \
                     tmp > lst[i-1][j] and tmp > lst[i+1][j]) else 0

print(res)

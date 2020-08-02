N = int(input())

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

M = int(input())
for _ in range(M):
    i, j, k = list(map(int, input().split()))
    i -= 1
    if j == 0:
        lst[i][:N-k], lst[i][N-k:] = lst[i][k:], lst[i][:k]
    else:
        lst[i][:k], lst[i][k:] = lst[i][N-k:], lst[i][:N-k]

res = 0
med = N // 2 + 1
j = N // 2
changed = False
for i in range(N):
    start, end = med-j-1, med+j
    res += sum(lst[i][start:end])
    if j == 0:
        changed = True
    if changed:
        j += 1
    else:
        j -= 1

print(res)
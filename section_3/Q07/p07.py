N = int(input())

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

res = 0
med = N // 2 + 1
j = 0
changed = False
for i in range(N):
    start, end = med-j-1, med+j
    res += sum(lst[i][start:end])
    if j == med - 1:
        changed = True
    if changed:
        j -= 1
    else:
        j += 1

print(res)


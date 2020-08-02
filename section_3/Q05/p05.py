N, M = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
for i in range(N):
    sum = 0
    for j in range(i, N):
        sum += lst[j]
        if sum == M:
            cnt += 1
            break

print(cnt)
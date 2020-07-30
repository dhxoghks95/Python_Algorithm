N = int(input("N 입력: "))

cnt = 0
total = 0
for i in range(N):
    tmp = int(input())
    if tmp == 1:
        cnt += 1
        total += cnt
    else:
        cnt = 0

print(total)
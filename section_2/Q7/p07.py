from time import perf_counter

N = int(input("N 입력: "))
cnt = 0

start = perf_counter()
for i in range(2, N+1):
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            break
    else:
        cnt += 1

end = perf_counter()
print(cnt, end - start)
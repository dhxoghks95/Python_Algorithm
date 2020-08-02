lst = list(range(1, 21))

for _ in range(10):
    start, end = map(int, input().split())
    lst[start-1:end] = lst[start-1:end][::-1]

print(*lst)
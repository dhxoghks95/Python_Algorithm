N = int(input("N 입력: "))
lst = []

for i in range(N):
    lst.append(int(input()))

avg = round(sum(lst) / N)
diff = float("Inf")

for i in range(N):
    tmp = abs(lst[i] - avg)
    if tmp < diff:
        diff = tmp
        index = i
    elif diff == tmp:
        index = max([index, i], key=lambda x: lst[x])

index += 1
print(f"Avg: {avg}, index: {index}, score: {lst[index-1]}")
N = int(input("N 입력: "))
K = int(input("K 입력: "))

lst = []
for i in range(N):
    lst.append(int(input()))

lst.sort(reverse=True)
maxSum = sum(lst[:2])
maxSum += lst[2:][K-1]

print(maxSum)




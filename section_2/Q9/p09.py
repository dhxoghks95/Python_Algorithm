def calPrize(lst):
    if len(set(lst)) == 1:
        return 10000 + lst[0] * 1000
    elif len(set(lst)) == 2:
        return 1000 + max(lst) * 100
    else:
        return max(lst) * 100


N = int(input("N 입력: "))
maximum = 0
for i in range(N):
    lst = []
    lst.append(int(input()))
    lst.append(int(input()))
    lst.append(int(input()))
    maximum = calPrize(lst) if calPrize(lst) > maximum else maximum


print(maximum)
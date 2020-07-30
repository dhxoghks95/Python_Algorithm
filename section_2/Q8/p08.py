def reverse(x):
    return int(x[::-1])


def isPrime(x):
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1

    return True


N = int(input("N 입력: "))
res = []

for i in range(N):
    tmp = input()
    if isPrime(reverse(tmp)):
        res.append(reverse(tmp))

for i in range(len(res)):
    print(res[i])

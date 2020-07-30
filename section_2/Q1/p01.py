N = input("N 입력: ")
K = input("K 입력: ")


def getK(N, K):
    N, K = int(N), int(K)
    cnt = 0
    for i in range(1, N):
        if N%i == 0:
            cnt +=1
        if cnt == K:
            return i
    return -1


print(getK(N, K))

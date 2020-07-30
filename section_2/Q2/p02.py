cnt = 0
T = int(input("T 입력: "))

while cnt < T:
    lst = []
    N = int(input("N 입력: "))
    s = int(input("s 입력: "))
    e = int(input("e 입력: "))
    k = int(input("k 입력: "))
    for i in range(N):
        lst.append(int(input()))
    lst = sorted(lst[s-1:e+1], reverse=True)

    cnt += 1
    print(f"#{cnt} {lst[k-1]}")

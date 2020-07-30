N = int(input("N 입력: "))


def digit_sum(x: str):
    return sum(map(int, x))


tmp_max = 0
for i in range(N):
    tmp = input()
    if digit_sum(tmp) > tmp_max:
        maximum = tmp
        tmp_max = digit_sum(tmp)

print(maximum)
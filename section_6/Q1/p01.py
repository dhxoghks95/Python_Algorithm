import sys

sys.stdin = open("./input1.txt", 'r')

N = int(input())
res = ''


def cal_binary(res, num):
    q, r = num // 2, num % 2
    res += str(r)
    if q == 1:
        res += str(q)
        return res
    else:
        return cal_binary(res, q)


print(cal_binary(res, N)[::-1])

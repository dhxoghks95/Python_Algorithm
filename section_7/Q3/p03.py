import sys

sys.stdin = open('./input3.txt', 'r')

k = int(input())
items = [int(x) for x in input().split()]
s = sum(items)
res = set()


def get_all(idx, tmp):
    if len(tmp) == len(items):
        if sum(tmp) > 0:
            res.add(sum(tmp))
        return
    else:
        # 곱하기 1
        get_all(idx+1, tmp+[items[idx]])
        # 곱하기 -1
        get_all(idx+1, tmp+[items[idx] * -1])
        # 안넣음(곱하기 0)
        get_all(idx+1, tmp+[items[idx] * 0])


get_all(0, [])
print(len(set(range(1, s+1))-res))

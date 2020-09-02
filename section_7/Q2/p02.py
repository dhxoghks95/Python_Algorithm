import sys

sys.stdin = open('./input2.txt', 'r')

n = int(input())
times = []
prices = []
for _ in range(n):
    time, price = [int(x) for x in input().split()]
    times.append(time)
    prices.append(price)
max_price = 0


def get_max(cur_idx, sum_price):
    global max_price
    if cur_idx >= n:
        if sum_price > max_price:
            max_price = sum_price
        return

    new_idx = cur_idx + times[cur_idx]
    # 현재 시점 포함
    get_max(new_idx, sum_price+prices[cur_idx])
    # 현재 시점 건너뜀
    get_max(cur_idx+1, sum_price)


get_max(0, 0)
print(max_price)

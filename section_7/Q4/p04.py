import sys

sys.stdin = open('./input4.txt', 'r')

total = int(input())
k = int(input())

prices = []
numbers = []
for _ in range(k):
    price, number = [int(x) for x in input().split()]
    prices.append(price)
    numbers.append(number)
cnt = 0


def get_num(idx, tmp_sum):
    global cnt
    if idx == k:
        if tmp_sum == total:
            cnt += 1
        return

    if tmp_sum > total:
        return

    for num in range(0, numbers[idx]+1):
        get_num(idx+1, tmp_sum + prices[idx] * num)


get_num(0, 0)
print(cnt)

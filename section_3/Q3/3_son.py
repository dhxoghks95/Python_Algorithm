import sys
# sys.stdin = open('input.txt', 'rt')

card = list(range(1,21))

for _ in range(10):
    a, b = map(int, input().split())
    order = range(a, b+1)

    tmp = []
    for i in order:
        tmp.append(card[i-1])
    for i, j in zip(order, tmp[::-1]):
        card[i-1] = j
print(*card)

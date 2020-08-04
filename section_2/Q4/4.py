import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
avg = round(sum(a)/n)
b = []

for i in range(n):
    b.append(a[i]-avg)

if 0 in b:
    print(avg, b.index(0)+1)
else:
    b_abs = [abs(number) for number in b]
    zip_b = zip(b, b_abs)
    sum = [x+y for (x,y) in zip_b]
    idx = min(x for x in sum if x != 0)
    print(avg, sum.index(idx)+1)

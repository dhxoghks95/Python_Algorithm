import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

def digit_sum(number):
    return sum(int(i) for i in str(number))

a_sum = [digit_sum(x) for x in a]
idx = a_sum.index(max(a_sum))
print(a[idx])

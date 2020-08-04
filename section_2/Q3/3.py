import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))
a_len = len(a)
b = list()

for idx1 in range(a_len):
    for idx2 in range(a_len):
        for idx3 in range(a_len):
            if idx1 != idx2 and idx1 != idx3 and idx2 != idx3:
                b.append(a[idx1]+a[idx2]+a[idx3])
b_unique = list(set(b))
b_unique.sort()
print(b_unique[-k])

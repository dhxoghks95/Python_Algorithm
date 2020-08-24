import sys

sys.stdin = open("./input5.txt", 'r')

C, N = list(map(int, input().split()))
s = []
for _ in range(N):
    s.append(int(input()))
max_sum = 0
total = sum(s)


def subset_sum(idx, cur_sum, tmp_sum):
    global max_sum
    if (cur_sum + total - tmp_sum) < max_sum:
        return
    elif cur_sum > C:
        return
    elif idx == N:
        if cur_sum > max_sum:
            max_sum = cur_sum
    else:
        subset_sum(idx+1, cur_sum+s[idx], tmp_sum+s[idx]) # tmp_sum 은 무조건 다 태움
        subset_sum(idx+1, cur_sum, tmp_sum+s[idx])


subset_sum(0, 0, 0)
print(max_sum)

import sys

sys.stdin = open("./input10.txt", "r")

N = int(input())
lst = list(map(int, input().split()))
new_lst = [N+1] * N
new_locations = set()

for i, e in enumerate(lst):
    for tmp_index in range(e, e + len(new_locations)+1):
        if tmp_index not in new_locations and \
            tmp_index - e == sum(map(lambda x: x < tmp_index, new_locations)):
            new_locations.add(tmp_index)
            new_lst[tmp_index] = i + 1
            break

print(*new_lst)
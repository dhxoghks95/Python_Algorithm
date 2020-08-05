import sys
sys.stdin = open("in5.txt", "r")

lst_len, target = map(int, input().split())
lst = sorted(list(map(int, input().split())))

def bin_search(num_lst, left, right, target):
    new_point = (left+right) // 2
    if num_lst[new_point] == target:
        return new_point + 1
    elif num_lst[new_point] > target:
        return bin_search(num_lst, left, (new_point-1),target)
    else:
        return bin_search(num_lst, (new_point+1), right, target)

print(bin_search(lst, 0, lst_len, target))


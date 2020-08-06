import sys
sys.stdin = open("in5.txt", "r")

line_num, target_num = map(int, input().split())
lines = [int(input()) for _ in range(line_num)]
denom_lst = list(range(max(lines)))

def count_made_lines(num_lst, denom):
    return sum([x // denom for x in num_lst])

def bin_search(num_lst, left, right, target, denom_lst, current):
    if right == left:
        return current + 1

    new_point = (left + right) // 2
    if count_made_lines(num_lst, denom_lst[new_point]) >= target:
        current = new_point
        return bin_search(num_lst, (new_point+1), right, target, denom_lst, current)
    else:
        return bin_search(num_lst, left, (new_point - 1), target, denom_lst, current)

print(bin_search(lines, 0, len(denom_lst), target_num, denom_lst, 0))

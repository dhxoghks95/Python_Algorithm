import sys
sys.stdin = open("in5.txt", "r")

lst_num = int(input())
lst = list(map(int, input().split()))

def pop_lst(value, list, word):
    if value == list[0]:
        word += "L"
        list.pop(0)
    else:
        word += "R"
        list.pop(-1)
    return list, word

how = ""
cnt = 0
prev = 0
while True:
    min_val = min(lst[0], lst[-1])
    max_val = max(lst[0], lst[-1])
    if min_val > prev :
        cnt += 1
        prev = min_val
        lst, how = pop_lst(min_val, lst, how)
    elif max_val > prev :
        cnt += 1
        prev = max_val
        lst, how = pop_lst(max_val, lst, how)
    else:
        break

print(cnt)
print(how)
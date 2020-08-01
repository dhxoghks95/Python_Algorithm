import sys
sys.stdin = open("in5.txt", "r")

first_len = int(input())
first_lst = list(map(int, input().split()))
sec_len = int(input())
sec_lst = list(map(int, input().split()))

if sec_len < first_len :
    for _ in range(sec_len):
        first_lst.append(sec_lst[0])
        sec_lst.pop(0)
    sorted_lst = sorted(first_lst)
else:
    for _ in range(first_len):
        sec_lst.append(first_lst[0])
        first_lst.pop(0)
    sorted_lst = sorted(sec_lst)

for elem in sorted_lst:
    print(elem, end = " ")
import sys
sys.stdin = open("in5.txt", "r")

len_lst, target = map(int, input().split(" "))
num_lst = list(map(int, input().split()))

cases = 0
left = 0
right = 1
sum = num_lst[0]
terminated = False

while not terminated:

    if sum < target:
        if right < len_lst:
            sum += num_lst[right]
            right += 1
        else:
            terminated = True

    else:
        if sum == target:
            cases += 1
        sum -= num_lst[left]
        left += 1

print(cases)

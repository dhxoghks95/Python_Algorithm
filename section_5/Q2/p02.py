import sys

sys.stdin = open("./input2.txt", "r")

lst = input()

lazers = {}
pipe_starts = []
pipes = {}
cnt = 0
for i in range(len(lst)-1):
    if lst[i] == '(' and lst[i+1] == ')':
        lazers[i] = i + 1

lazers_ = lazers.keys() | lazers.values()
for i in range(len(lst)):
    if i in lazers_:
        continue
    elif lst[i] == '(':
        pipe_starts.append(i)
        cnt += 1
    else:
        pipes[pipe_starts.pop()] = i

res = 0
for k, v in pipes.items():
    cnt = 1
    for start, end in lazers.items():
        if (k < start) and (v > end):
            cnt += 1
    res += cnt

print(res)



import sys

sys.stdin = open("./input7.txt", "r")
order = input()
l  = int(input())

for i in range(1, l+1):
    tmp = input()
    cnt = 0
    right = True
    for s in tmp:
        if s in order and s != order[cnt]:
            right = False
            break
        elif s in order and s == order[cnt]:
            cnt += 1
        else:
            continue

    if right:
        print(f"#{i} YES")
    else:
        print(f"#{i} NO")
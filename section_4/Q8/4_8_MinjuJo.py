import sys
sys.stdin = open("in5.txt", "r")

ppl_num, max_weight = map(int, input().split())
ppl_lst = sorted(list(map(int, input().split())))

cnt = 0
terminated = False

while not terminated:
    if ppl_lst[0] + ppl_lst[-1] <= max_weight:
        ppl_lst.pop(0)
    ppl_lst.pop(len(ppl_lst) - 1)
    cnt +=1

    if len(ppl_lst) == 1:
        cnt+=1
        terminated = True

    if len(ppl_lst) == 0:
        terminated = True

print(cnt)
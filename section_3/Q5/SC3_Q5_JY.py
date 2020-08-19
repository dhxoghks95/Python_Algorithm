import sys
#sys.stdin=open("input.txt","rt")

N, M = map(int, input().split())
lst = list(map(int, input().split()))

lt=0
rt=1
tot=lst[0]
cnt=0
while True:
    if tot<M:
        if rt<N:
            tot+=lst[rt]
            rt+=1
        else : break
    elif tot==M:
        cnt+=1
        tot-=lst[lt]
        lt+=1
    else:
        tot-=lst[lt]
        lt+=1
print(cnt)
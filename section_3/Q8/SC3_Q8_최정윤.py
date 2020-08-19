import sys
#sys.stdin=open("input.txt","rt")

N= int(input())

mtx = [list(map(int, input().split())) for _ in range(N)]

M=int(input())
for i in range(M):
    r,d,s=map(int,input().split())
    if d==0:
        for _ in range(s):
            mtx[r-1].append(mtx[r-1].pop(0))
    else:
        for _ in range(s):
            mtx[r-1].insert(0, mtx[r-1].pop())


st=0
end=N-1
tot=0
for i in range(N):
    for j in range(st,end+1):
        tot+=mtx[i][j]
    if i<N//2:
        st+=1
        end-=1
    else:
        st-=1
        end+=1

print(tot)
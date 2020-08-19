import sys
#sys.stdin=open("input.txt","rt")

N= int(input())

mtx = [list(map(int, input().split())) for _ in range(N)]
mtx.insert(0, [0]*N)
mtx.append([0]*N)
for i in range(N+2):
    mtx[i].insert(0,0)
    mtx[i].append(0)

x=[-1,0,1,0]
y=[0,1,0,-1]

cnt=0
for i in range(1,N+1):
    for j in range(1,N+1):
        if all(mtx[i][j]>mtx[i+x[k]][j+y[k]] for k in range(4)):
            cnt+=1
print(cnt)
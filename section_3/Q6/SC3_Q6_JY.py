import sys
#sys.stdin=open("input.txt","rt")

N= int(input())

mtx=[]
for i in range(N):
    lst=list(map(int,input().split()))
    mtx.append(lst)


def max_sum(x):
    tot=[]
    for i in range(N):
        tot.append(sum(x[i]))

    ve_sum=[]
    for i in range(N):
        sums=0
        for j in range(N):
            sums+=x[j][i]
        tot.append(sums)

    sums=0
    for i in range(N):
        sums+=x[i][i]
    tot.append(sums)
    print(max(tot))

max_sum(mtx)


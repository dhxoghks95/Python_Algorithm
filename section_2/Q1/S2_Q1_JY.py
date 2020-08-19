import sys
#sys.stdin=open("input.txt","rt")


N,K=input().split(' ')
N=int(N)
K=int(K)
count=0
for i in range(N):
    i+=1
    if N%i==0:
        count+=1
    if count==K:
        print(i)
        break
else: print(-1)










import sys
#sys.stdin=open("input.txt","rt")

N,M=map(int,input().split())
total=[]
for i in range(1,N+1):
    for j in range(1,M+1):
        total.append(i+j)
nums=(set(filter(lambda x: total.count(x)==max(total.count(i) for i in set(total)),total)))
print(' '.join(str(i) for i in nums))


















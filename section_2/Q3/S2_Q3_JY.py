import sys
#sys.stdin=open("input.txt","rt")


N,K=map(int,input().split())
cards=list(map(int, input().split()))
total=set()
for i in range(N):
    for j in range(i+1,N):        
        for r in range(j+1,N):
            total.add(cards[i]+cards[j]+cards[r])
print(sorted(total,reverse=True)[K-1])















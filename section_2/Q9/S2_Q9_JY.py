import sys
#sys.stdin=open("input.txt","rt")

N=int(input())
lst=[]
for i in range(1,N+1):
    reward=0
    n=list(map(int,input().split()))
    if n[0]==n[1] and n[0]==n[2]:
        reward=10000+n[0]*1000
    elif n[0]==n[1] and n[0]!=n[2]:
        reward=1000+n[0]*100
    elif n[0]==n[2] and n[0]!=n[1]:
        reward=1000+n[0]*100
    elif n[1]==n[2] and n[1]!=n[0]:
        reward=1000+n[1]*100
    else: reward= max(n)*100
    lst.append(reward)
print(max(lst))




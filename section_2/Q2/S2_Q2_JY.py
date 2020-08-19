import sys
#sys.stdin=open("input.txt","rt")


T=int(input())
for i in range(T):
    N,s,e,k=map(int,input().split())
    n=list(map(int,input().split()))
    i+=1
    print('#'+str(i)+' '+str(sorted(n[s-1:e])[k-1]))












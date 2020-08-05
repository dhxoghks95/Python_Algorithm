import sys
#sys.stdin=open("input.txt","rt")

N1=int(input())
lst1=list(map(int,input().split()))
N2=int(input())
lst2=list(map(int,input().split()))
lst=sorted(lst1+lst2)
for i in lst:
    print(i,end=' ')
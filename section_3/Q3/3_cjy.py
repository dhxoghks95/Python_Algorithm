import sys
#sys.stdin=open("input.txt","rt")

lst=list(range(1,21))
cnt=0
while cnt<10:
    start,end=map(int,input().split())
    lst[start-1:end]=list(reversed(lst[start-1:end]))
    cnt+=1
for i in lst:
    print(i, end=' ')
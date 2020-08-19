import sys
#sys.stdin=open("input.txt","rt")

N=int(input())

lst=list(map(int,input().split()))
cnt=0
score=[]
for i in lst:
    if i==1:
        if cnt==0:
            score.append(1)
        else:
            score.append(1+score[cnt-1])
    else:
        score.append(0)
    cnt+=1
print(sum(score))


      







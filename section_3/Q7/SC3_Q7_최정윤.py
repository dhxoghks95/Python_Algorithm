import sys
#sys.stdin=open("input.txt","rt")

N= int(input())

mtx=[]
for i in range(N):
    lst=list(map(int,input().split()))
    mtx.append(lst)

idx=[]
x=N//2
st=x
end=x
for i in range(N):
    if i==0 or i==N-1:
        idx.append(x)
    elif i<=x:
        st-=1
        end+=1
        idx.append([st,end])
    else:
        st+=1
        end-=1
        idx.append([st,end])

tot=[]
for i in range(N):
    if i==0 or i==N-1:
        tot.append(mtx[i][idx[i]])
    else: tot.append(sum(mtx[i][idx[i][0]:idx[i][1]+1]))
print(sum(tot))


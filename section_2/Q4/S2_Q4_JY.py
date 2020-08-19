import sys
#sys.stdin=open("input.txt","rt")

N=int(input())
grades=list(map(int,input().split()))
mean=int(round(sum(grades)/len(grades),0))
differ=[]
for i in grades:
    differ.append(abs(i-mean))
mean_list=list(grades[i] for i, value in enumerate(differ) if value == min(differ))
print(str(mean)+' '+str(grades.index(max(mean_list))+1))
















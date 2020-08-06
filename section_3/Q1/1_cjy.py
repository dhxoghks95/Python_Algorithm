import sys
#sys.stdin=open("input.txt","rt")

N=int(input())


for i in range(1,N+1):
    lst=str(input()).lower()
    if lst==lst[::-1]:
        print("#{}".format(i)+" "+"YES")
    else: print("#{}".format(i)+" "+"NO")



      







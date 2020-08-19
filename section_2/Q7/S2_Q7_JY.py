import sys
#sys.stdin=open("input.txt","rt")

N=int(input())

def prime(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return(len(num))   

print(prime(N))


               




            


















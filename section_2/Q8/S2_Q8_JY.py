import sys
#sys.stdin=open("input.txt","rt")

N=int(input())
nums=list(map(int,input().split()))

def reverse(x):
    reversed=[]
    for i in nums:
        reversed.append(int(str(i)[::-1].lstrip("0")))
    return(reversed)
    

def isPrime(x):
    for i in x:
        bool = True
        if i==1: bool=False
        for j in range(2,int(i**(0.5))+1):
            if i%j==0:
                bool= False
        if bool == True:
            print(i,end=' ')
    

isPrime(reverse(nums))

















import sys
#sys.stdin=open("input.txt","rt")

x=list(filter(str.isdigit, str(input())))
def divisor(x):
    cnt=0
    for i in range(1,x+1):
        if x%i==0:
            cnt+=1
    print(x)
    print(cnt)

divisor(int("".join(x)))


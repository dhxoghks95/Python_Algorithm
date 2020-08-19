import sys
#sys.stdin=open("input.txt","rt")

def digit_sum(x,nums):
    total=[]
    for j in nums:
        digits=list(str(j))
        sum_digits=0
        for k in digits:
            sum_digits+=int(k)
        total.append(sum_digits)
    return(nums[total.index(max(total))])

print(digit_sum(int(input()),list(map(int,input().split()))))


















import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
k = list(map(int, input().split()))

def reverse(x):
    tmp = [i for i in str(x)]
    tmp = reversed(tmp)
    rev_num = int(''.join(tmp))
    return rev_num

def isPrime(x):
    if x > 1:
        for i in range(2,x):
            if x % i == 0:
                break
        else:
            return x

answer = []
for idx in range(n):
    answer.append(isPrime(reverse(k[idx])))
answer = [i for i in answer if i]
print(*answer)

import sys
sys.stdin = open("input.txt", "rt")
# https://wikidocs.net/21638 참고

n = int(input())
a = [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i-2]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j-2] = False

print(len(primes))

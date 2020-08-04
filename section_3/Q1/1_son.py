import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())

for n in range(N):
    word = input().lower()
    if word == word[::-1]:
        print('#%d YES' %(n+1))
    else:
        print('#%d NO' %(n+1))

import sys
# sys.stdin = open('input.txt', 'rt')

n1 = int(input())
list1 = list(map(int, input().split()))
n2 = int(input())
list2 = list(map(int, input().split()))

answer = list1 + list2
answer.sort()
print(*answer)

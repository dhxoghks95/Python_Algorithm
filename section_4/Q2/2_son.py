import sys
sys.stdin = open('input.txt', 'rt')

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
cnt = 0
answer = 0

lt = 1
rt = int(sum(lan)/n) #최대 가능

while lt <= rt:
    cnt = 0
    mid = (lt+rt)//2
    for i in lan:
        cnt += (i//mid)
    if cnt >= n:
        answer = mid
        lt = mid+1
    else:
        rt = mid-1
print(answer)

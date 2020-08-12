import sys
sys.stdin = open('input.txt','r')

n, c = map(int, input().split())
barn = [int(input()) for _ in range(n)] #마굿간 위치
barn.sort()
print(barn)

#거리를 len으로 했을 때, 배치할 수 있는 말(horse)의 개체 수 세기
def Count(len):
    cnt=1
    horse = barn[0]
    for i in range(1, n):
        if barn[i]-horse >= len:
            cnt+=1 #한 마리 배치함
            horse = barn[i]
    return cnt #총 몇 마리 배치했는지 return

lt = 1
rt = barn[n-1]-1 #맨마지막 위치-맨첫번째 위치(lt)
answer = 0
while lt <= rt:
    mid = (lt+rt) // 2
    print(mid)
    if Count(mid) >= c:
        answer = mid
        lt = mid+1
    else:
        rt = mid-1
print(answer)

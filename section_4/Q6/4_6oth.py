import sys
sys.stdin = open('C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 4/6. 씨름선수/in1.txt', 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


a.sort()
a
height = min
cnt = 0
for x, y in a:
    if y > height:
        height = y
        cnt += 1

print(cnt)
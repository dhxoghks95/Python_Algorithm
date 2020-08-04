import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/6. 격자판 최대합/in1.txt","rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

summation = list()
cross = list()
rcross = list()
for i in range(n):
    summation.append(sum(a[i][:]))
    summation.append(sum(a[:][i]))
    cross.append(a[i][i])
    reverse = list(range(n, 0, -1))
    j = reverse[i-1] - 1
    rcross.append(a[i][j])


summation.append(sum(cross))
summation.append(sum(rcross))

max(summation)
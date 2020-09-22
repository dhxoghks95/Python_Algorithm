"""
Section 6 -Q6

중복순열 구하기

1부터 N까지 번호가 적힌 구슬이 있습니다.
이 중 중복을 허락하여 M번을 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
"""

import sys
sys.stdin = open('input.txt', 'r')

def DFS(d): # d=0,1,2 : 상태트리의 depth, 그리고 res의 인덱스
    global cnt
    # 종착점 즉 터미널 노드일 때
    if d==m:
        # res의 원소들을 옆으로 출력
        for i in range(m):
            print(res[i], end=' ')
        print()
        # 정답 개수 1 증가
        cnt += 1
    # 상태트리 탐색
    else:
        for i in range(1, n+1): # i=1,2,3
            res[d] = i
            DFS(d+1)

if __name__=='__main__':
    n, m = map(int, input().split(' ')) # n=3, m=2
    res = [0] * m # res=[0,0] : 출력하고 싶은 정답값
    cnt = 0
    DFS(0)
    print(cnt)

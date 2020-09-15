"""
Section 6 - Q8

순열 구하기

1부터 N까지 번호가 적힌 구슬이 있습니다.
이중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
"""

import sys
sys.stdin = open('input.txt', 'r')

def DFS(x):
    global cnt
    if x==m:
        for i in res:
            print(i, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1): # i=1,2,3
            if ch[i]==0:
                res[x] = i
                ch[i] = 1 # 1을 선택했을 때 또다시 1을 선택하지 않도록 1로 체크
                DFS(x+1)
                ch[i] = 0 # 1을 다 돌고 나면 2,3을 돌 때에는 1을 사용할 수 있도록 0으로 체크

if __name__=='__main__':
    n, m = map(int, input().split(' '))
    res = [0] * m
    ch = [0] * (n+1) # 체크 변수
    cnt = 0
    DFS(0)
    print(cnt)

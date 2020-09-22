"""
Section 6 - Q3

부분집합 구하기(DFS)

자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램 을 작성하세요.
"""

import sys
sys.stdin = open('input.txt', 'r')

def DFS(d):
    # 종착점 즉 터미널 노드일 때
    if d==n+1: # d==4일 때
        # 체크 변수에서 값이 1인 원소들만 출력
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    # 상태트리 탐색
    else:
        ch[d] = 1 # 원소를 사용하겠다! 하여 1을 값으로 할당
        DFS(d+1) # 가지 뻗기 ㄱ
        ch[d] = 0 # 원소를 사용하지 않겠다! 하여 0을 값으로 할당
        DFS(d+1) # 가지 뻗기 ㄱ

if __name__=='__main__':
    n = int(input()) # n=3
    ch = [0] * (n+1) # ch=[0,0,0,0] : 원소를 사용하겠다! 사용하지 않겠다!를 1, 0으로 체크할 체크 변수
    DFS(1)

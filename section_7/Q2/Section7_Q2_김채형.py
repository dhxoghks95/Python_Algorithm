"""
Section 7 - Q2

휴가(삼성 SW역량평가 기출문제 : DFS활용)
"""

import sys
sys.stdin = open('input.txt', 'r')

def DFS(d, total):
    global res
    # 종착점 (T, P에 맨앞에 0 삽입했으므로 n+1까지 가야 터미널 노드임)
    if d==n+1:
        if total>res:
            res = total
    else:
        # d일 상담을 하는 경우
        if d+T[d] <= n+1: # T, P에 맨앞에 0 삽입했으므로 n+1로 해야 7일까지 읽을 수 있음
            DFS(d+T[d], total+P[d])
        # d일 상담 하지 않는 경우
        DFS(d+1, total)

if __name__=='__main__':
    n = int(input()) # n=7
    T = list()
    P = list()
    for _ in range(n):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)
    T.insert(0, 0) # 1일을 인덱스 1로 맞춰주기 위해서
    P.insert(0, 0) # 1일을 인덱스 1로 맞춰주기 위해서
    res = 0 # 정답
    DFS(1, 0)
    print(res)

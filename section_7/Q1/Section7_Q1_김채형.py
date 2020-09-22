"""
Section 7 - Q1

최대점수 구하기(DFS)

이번 정보올림피아드대회에서 좋은 성적을 내기 위하여 현수는 선생님이 주신 N개의 문제를 풀려고 합니다.
각 문제는 그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 됩니다.
제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야 합니다.
(해당문제는 해당시간이 걸리면 푸는 걸로 간주한다, 한 유형당 한개만 풀 수 있습니다.)
"""

import sys
sys.stdin = open('input.txt', 'r')

def DFS(d, score, time): # d = 0,1,2,3,4 => 문제 1,2,3,4,5

    global res

    if time > m: # 시간 초과하면
        return # 가지치기

    if d==n: # 종착점
        if score>res:
            res = score

    else:
        DFS(d+1, score+score_ls[d], time+time_ls[d]) # d번째 문제를 풀고 넘긴다!
        DFS(d+1, score, time) # d번째 문제를 안 풀고 넘긴다!

if __name__=='__main__':
    n, m = map(int, input().split(' '))  # n=5, m=20(제한시간)
    score_ls = []
    time_ls = []
    for _ in range(n):
        a, b = map(int, input().split(' ')) # 점수, 시간
        score_ls.append(a)
        time_ls.append(b)
    res = float('-inf')
    DFS(0, 0, 0)
    print(res)

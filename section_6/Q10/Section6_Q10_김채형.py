"""
Section 6 - Q10

조합 구하기

1부터 N까지 번호가 적힌 구슬이 있습니다.
이중 M개를 뽑는 방법의 수를 출력하는 프로그램을 작성하세요.
"""

import sys
sys.stdin = open('input.txt', 'r')

def DFS(d, s):

    global cnt

    if d==m:
        for ele in res:
            print(ele, end=' ')
        print()
        cnt += 1

    else:
        for i in range(s, n+1):
            if ch[i]==0:
                res[d] = i
                ch[i] = 1
                DFS(d+1, i+1)
                ch[i] = 0

if __name__=='__main__':
    n, m = map(int, input().split(' ')) # n=4, m=2
    res = [0] * m
    ch = [0] * (n+1)
    cnt = 0
    DFS(0, 1)
    print(cnt)

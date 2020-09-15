"""
Section 6 - Q9

수열 추측하기
"""

import sys
sys.stdin = open('input.txt', 'r')

def DFS(x, total):

    # 종착점 + 값이 일치할 때
    if x == n and total == f:
        for ele in seq:
            print(ele, end=' ')
        sys.exit() # 코드 종료

    else:
        for i in range(1, n+1): # i=1,2,3,4
            if ch[i] == 0:
                ch[i] = 1 # 사용했다! 로 체크
                seq[x] = i # 수열 만들기
                tot = seq[x]*b[x]
                DFS(x+1, total+tot)
                ch[i] = 0 # 사용 안 했다! 로 초기화

if __name__ == "__main__":
    n, f = map(int, input().split()) # n=4, f=16
    seq = [0] * n # seq = [0,0,0,0] : 수열 초기화
    b = [1] * n # b = [1,1,1,1] : 계수 초기화
    for i in range(1, n):
        b[i] = int(b[i-1] * (n-i)/i)
    #print(b)
    ch = [0] * (n+1) # 체크 변수
    DFS(0, 0) # b[1]*seq[1] +

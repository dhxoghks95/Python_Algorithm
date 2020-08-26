import sys
sys.stdin = open('C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 6/6. 중복순열 구하기/in1.txt', 'rt')

def DFS(v):
    global cnt
    if v == m:
        for i in range(m):
            print(res[i], end = ' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            res[v] = i
            DFS(v+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n
    cnt = 0
    DFS(0)
    print(cnt)
import sys
sys.stdin = open('C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 6/4. 합이 같은 부분집합/in1.txt', 'rt')



def DFS(v, sum):
    if sum>total//2:
        return
    if v == n:
        if sum == (total - sum):
            print('YES')
            sys.exit(0)


    else:
        DFS(v+1, sum + a[v])
        DFS(v+1, sum)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")




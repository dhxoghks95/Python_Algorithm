import sys
import heapq as hq
sys.stdin=open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/10. 최소힙/in1.txt", "r")
a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)


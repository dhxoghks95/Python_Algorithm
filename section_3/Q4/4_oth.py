import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/4. 두 리스트 합치기/in1.txt","rt")
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

c = a+b
c.sort()
print(c)
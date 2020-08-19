import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/8. 단어찾기/in1.txt","rt")

n = int(input())

a = [input() for _ in range(n)]

poem = [input() for _ in range(n-1)]

for n in a:
    if all(n != x for x in poem):
        print(n)

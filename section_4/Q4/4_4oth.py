import sys
sys.stdin = open('C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 4/4. 마구간 정하기/in1.txt', 'rt')

n, c = map(int, input().split())

horse = list()

for i in range(n):
    horse.append(int(input()))

def combi(s = list()):
    com = []
    for i in range(len(s)):

            
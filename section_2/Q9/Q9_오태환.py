import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/9. 주사위 게임/in1.txt","rt")

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]


def money(x= list()):
    number = list()
    maximum = 0
    for i in range(1, max(x)+1): 
        if x.count(i) >= maximum:
            maximum = x.count(i)
            num = i
            number.append(i)
    if maximum == 3:
        return 10000 + num * 1000
    if maximum == 2:
        return 1000 + num * 100
    if maximum == 1:
        return 100 * max(number)


maximum = 0

for i in range(n):
    b = a[i]
    if money(b) > maximum:
        maximum = money(b)

print(maximum)
    
    
        

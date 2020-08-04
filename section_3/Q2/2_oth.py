import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/2. 숫자만 추출/in1.txt","rt")
n = str(input())

number = list()

for i in range(len(n)):
    if n[i].isalpha() == False:
        number.append(int(n[i]))

num = 0
for i in range(len(number)):
    num += number[i] * 10 ** (len(number) - i - 1)


yaksu = list()
for i in range(1, num+1):
    if num % i == 0:
        yaksu.append(i)

print(num,'\n',len(yaksu))

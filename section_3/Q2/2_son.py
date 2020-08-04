import sys
#sys.stdin = open('input.txt', 'rt')

a = str(input())
a_list = [x for x in a]
answer1 = []
answer2 = 0

for k in a_list:
    if k.isdigit(): #숫자인지 판별하는 함수
        answer1.append(k)
answer1 = int(''.join(answer1))

for i in range(1, answer1+1):
    if answer1 % i == 0:
        answer2 += 1

print(answer1)
print(answer2)

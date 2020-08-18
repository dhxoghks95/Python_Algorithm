"""
Section 3 - Q2

숫자만 추출

문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만듭니다.
만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 됩니다.
즉 첫 자리 0은 자연수화 할 때 무시합니다.
출력은 120를 출력하고, 다음 줄에 120 의 약수의 개수를 출력하면 됩니다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.
"""
import sys

sys.stdin = open('input.txt', 'r')
string = str(input())

scalar = ''
for i in range(len(string)):
    if string[i].isdigit():
        scalar += string[i]
    if scalar.startswith('0'):
        scalar.replace('0', '')
scalar = int(scalar)

cnt = 0
for i in range(1, scalar+1):
    if scalar % i == 0:
        cnt += 1

print(scalar)
print(cnt)

"""
s = '123abc'
i = int(filter(str.isdigit,s))
print(i)
"""
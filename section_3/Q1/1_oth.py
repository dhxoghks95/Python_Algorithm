import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/1. 회문 문자열 검사/in1.txt","rt")
n = int(input())
a = [list(map(str, input())) for _ in range(n)]

def reverse(x = list()):
    back = list()
    for i in range(len(x), 0, -1):
        back.append(x[i-1])

    return back

def all_lower(x = list()):
    to_lower = list()
    for i in range(len(x)):
        to_lower.append(x[i].lower())
    return to_lower

for i in range(n):
    if all_lower(a[i]) == all_lower(reverse(a[i])):
        print('YES')
    else:
        print("NO")




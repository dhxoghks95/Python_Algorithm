import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/3. 카드 역배치/in1.txt","rt")
a = [list(map(int, input().split())) for _ in range(10)]


card = list(range(1, 21))


def reverse(x = list()):
    back = list()
    for i in range(len(x), 0, -1):
        back.append(x[i-1])
    return back


for i in range(len(a)):
    section = a[i]
    forward = card[:section[0]-1]
    mid = reverse(card[section[0]-1:section[1]])
    backward = card[section[1]:]
    card = forward + mid + backward

print(card)

import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/10. 스도쿠 검사/in3.txt", 'rt')

a = [list(map(int, input().split())) for _ in range(9)]
a
def three_by_three(s = list(), i=0, j=0):
    three_by_three = s[i][j:j+3] + s[i+1][j:j+3]+ s[i+2][j:j+3]
    return three_by_three
   

def unique(s = list()):
    cnt = 0
    for i in range(len(s)):
        cnt += s.count(s[i])

    if cnt == len(s):
        return True
    else:
        return False

def sdoku(a):
    for i in range(0, len(a), 3):
        for j in range(0, len(a), 3):
            if unique(three_by_three(a, i, j)) == False:
                return 'NO'
                break            
    else:
        return 'YES'

sdoku(a)
import sys
#sys.stdin = open('input.txt', 'r')

tmp = []; tmp1 = []; tmp2 = []; tmp3 = []; tmp4 = [];
tmp5 = []; tmp6 = []; tmp7 = []; tmp8 = []; tmp9 = [];
answer = 0
#1~9 모두 포함여부 확인함수
def check(a):
    if ((1 in a) and (2 in a) and (3 in a) and (4 in a) and (5 in a)
    and (6 in a) and (7 in a) and (8 in a) and (9 in a)):
        return True

# matrix 만들기
mat = [list(map(int, input().split())) for _ in range(9)]

# 행, 열, 3x3보드 확인
for i in range(9):
    if check(mat[i]):
        answer += 1 # 행 확인
    for j in range(9):
        tmp.append(mat[j][i])
        if len(tmp) == 9 and check(tmp):
            answer += 1 # 열 확인
            tmp = []

for x in range(9): #3x3보드 확인
    for y in range(9):
        if x<3 and y<3:
            tmp1.append(mat[x][y])
            if len(tmp1) == 9 and check(tmp1):
                answer += 1
        elif x<3 and y<6:
            tmp2.append(mat[x][y])
            if len(tmp2) == 9 and check(tmp2):
                answer += 1
        elif x<3 and y<9:
            tmp3.append(mat[x][y])
            if len(tmp3) == 9 and check(tmp3):
                answer += 1
        elif x<6 and y<3:
            tmp4.append(mat[x][y])
            if len(tmp4) == 9 and check(tmp4):
                answer += 1
        elif x<6 and y<6:
            tmp5.append(mat[x][y])
            if len(tmp5) == 9 and check(tmp5):
                answer += 1
        elif x<6 and y<9:
            tmp6.append(mat[x][y])
            if len(tmp6) == 9 and check(tmp6):
                answer += 1
        elif x<9 and y<3:
            tmp7.append(mat[x][y])
            if len(tmp7) == 9 and check(tmp7):
                answer += 1
        elif x<9 and y<6:
            tmp8.append(mat[x][y])
            if len(tmp8) == 9 and check(tmp8):
                answer += 1
        elif x<9 and y<9:
            tmp9.append(mat[x][y])
            if len(tmp9) == 9 and check(tmp9):
                answer += 1

if answer == 27:
    print('YES')
else:
    print('NO')

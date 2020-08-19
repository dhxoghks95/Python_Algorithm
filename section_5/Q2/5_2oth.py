import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/2. 쇠막대기/in1.txt","rt")

pipe = input()
pipe
cut = []
cnt = 0

for i in range(len(pipe)):
    if pipe[i] == '(':
        cut.append(pipe[i])
    else:
        cut.pop()
        if pipe[i-1] == '(':
            cnt += len(cut)
        else:
            cnt += 1

print(cnt)

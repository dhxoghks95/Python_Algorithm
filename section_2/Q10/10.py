import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
sol = list(map(int, input().split()))
score = []

#idx = 0일 때,
if sol[0] == 1:
    score.append(1)
else:
    score.append(0)
#idx > 0일 때,
for idx in range(1,n):
    if sol[idx] == 1:
        score.append(score[idx-1] + 1)
    else:
        score.append(0)
print(sum(score))

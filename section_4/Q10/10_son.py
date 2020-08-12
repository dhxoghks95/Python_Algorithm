import sys
# sys.stdin = open('input.txt','r')

n = int(input())
seq = list(map(int, input().split())) #reverse sequence
answer = [0]*n

# 5 3 4 0 2 1 1 0 (seq)
# 0 0 0 0 0 0 0 0 (answer)
#

for i in range(n):
    for j in range(n):
        if (answer[j]==0) & (seq[i]==0):
            answer[j] = i+1
            break # 여기 이후부터는 답 보고 함...
        elif answer[j] == 0:
            seq[i] -= 1
print(*answer)

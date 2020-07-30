N = int(input("N 입력: "))
M = int(input("M 입력: "))

probs = {x: 0 for x in range(2, N+M+1)}

for i in range(1, N+1):
    for j in range(1, M+1):
        probs[i+j] += 1

maxProb = max(probs.values())
print(' '.join([str(x) for x in probs if probs[x] == maxProb]))



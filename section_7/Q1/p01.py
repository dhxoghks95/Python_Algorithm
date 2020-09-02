import sys

sys.stdin = open('./input1.txt', 'r')

n, m = [int(x) for x in input().split()]
scores = []
times = []

for _ in range(n):
    score, time = [int(x) for x in input().split()]
    scores.append(score)
    times.append(time)
max_score = 0


def get_max(idx, tmp_scores, tmp_times):
    global max_score
    if sum(tmp_times) > m:
        return
    # 다봤음
    if idx == n-1:
        if sum(tmp_scores) > max_score:
            max_score = sum(tmp_scores)
        return

    get_max(idx+1, tmp_scores[:] + [scores[idx+1]], tmp_times[:] + [times[idx+1]])
    get_max(idx+1, tmp_scores[:], tmp_times[:])


get_max(-1, [], [])
print(max_score)

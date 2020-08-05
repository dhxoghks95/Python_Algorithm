import sys
sys.stdin = open("in5.txt", "r")

cand_num = int(input())
info = []
for _ in range(cand_num):
    hei, wei = map(int, input().split())
    info.append((hei, wei))

info = sorted(info) # sorted by height
weight = [x[1] for x in info] # weights of candidates - sorted by their heights
cnt = 1 # tallest candidate

for i in range(cand_num - 1): # except the tallest candidate
    if weight[i] > max(weight[i+1:]): # if there's no candidate heavier than this candidate
        cnt += 1

print(cnt)
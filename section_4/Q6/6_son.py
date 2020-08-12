import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
player = []
for _ in range(n):
    x, y = map(int, input().split())
    player.append((x, y))
player.sort(key=lambda x:-x[0]) #reverse=True
# print(player)

last_w = 0
cnt = 0
for height, weight in player:
    if weight > last_w:
        last_w = weight
        cnt += 1
print(cnt)




# cnt = 0
# for h, w in player:
#     if (h >= h_zip[w_i])|(w >= w_zip[h_i]):
#         cnt += 1
        # print(h, w)
# print(cnt)



# h_zip = []
# w_zip = []
# for height, weight in player:
#     h_zip.append(height)
#     w_zip.append(weight)
# print(h_zip)
# print(w_zip)
#
# cnt = 0
# maxh_idx = h_zip.index(max(h_zip)) #가장 큰 키를 가진 사람의 index
# std_w = w_zip[maxh_idx] #std_w: standard weight(몸무게 기준치)
# maxw_idx = w_zip.index(max(w_zip)) #가장 무거운 몸무게를 가진 사람의 index
# std_h = h_zip[maxw_idx] #std_h: standard height(키 기준치)
# print(std_w)
# print(std_h)
#
# player1 = []
# for i in range(n):
#     if (w_zip[i] > std_w) | (h_zip[i] > std_h):
#         player1.append(player[i])
# print(player1)

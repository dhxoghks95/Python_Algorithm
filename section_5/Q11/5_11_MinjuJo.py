import sys
import heapq as hq
sys.stdin = open("in5.txt", "r")
max_heap = []

while True:
    num = int(input())
    if num == -1:
        break
    elif num == 0:
        try:
            print(hq.heappop(max_heap)[1])
        except:
            print(-1)
    else:
        hq.heappush(max_heap, (-num, num))

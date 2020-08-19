import heapq as hq
import sys
sys.stdin = open("in5.txt", "r")

min_heap = []
while True:
    num = int(input())
    if num == -1:
        break
    elif num == 0:
        try:
            print(hq.heappop(min_heap))
        except:
            print(-1)
    else:
        hq.heappush(min_heap, num)
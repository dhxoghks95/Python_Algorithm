import sys

sys.stdin = open("./input5.txt", "r")

N, K = list(map(int, input().split()))


class Queue:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def pop(self, i):
        res = self.lst.pop(i)
        self.lst = self.lst[i:] + self.lst[:i]
        return res


queue = Queue(list(range(1, N+1)))

while len(queue) > K-1:
    queue.pop(K-1)

print(queue.lst[-1])

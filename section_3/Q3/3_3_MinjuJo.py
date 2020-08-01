import sys
sys.stdin = open("in2.txt", "r")
lst = list(range(21))

for i in range(10):
    start, fin = map(int, input().split(" "))
    lst[start:fin+1] = lst[fin:start-1:-1]

lst.pop(0)

for elem in lst:
    print(elem, end = ' ')


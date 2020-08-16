import sys

sys.stdin = open("./input10.txt", "r")

lst = [float("-Inf")]
res = []
while True:
    tmp = int(input())
    if tmp == -1:
        break
    elif tmp == 0:
        lst[1], lst[-1] = lst[-1], lst[1]
        res.append(lst.pop())
        i = 1
        while True:
            left, right = 2*i, 2*i+1
            smallest = i
            if left < len(lst) and lst[smallest] > lst[left]:
                smallest = left
            if right < len(lst) and lst[smallest] > lst[right]:
                smallest = right

            if smallest != i:
                lst[i], lst[smallest] = lst[smallest], lst[i]
                i = smallest
            else:
                break
    else:
        lst.append(tmp)
        i = len(lst) - 1
        while i > 1:
            if lst[i//2] > lst[i]:
                lst[i], lst[i//2] = lst[i//2], lst[i]
                i //= 2
            else:
                break

print(*res, sep='\n')

import sys

sys.stdin = open("./input11.txt", "r")

lst = [float("Inf")]
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
            largest = i
            if left < len(lst) and lst[largest] < lst[left]:
                largest = left
            if right < len(lst) and lst[largest] < lst[right]:
                largest = right

            if largest != i:
                lst[i], lst[largest] = lst[largest], lst[i]
                i = largest
            else:
                break
    else:
        lst.append(tmp)
        i = len(lst) - 1
        while i > 0:
            if lst[i//2] < lst[i]:
                lst[i], lst[i//2] = lst[i//2], lst[i]
                i //= 2
            else:
                break

print(*res, sep='\n')

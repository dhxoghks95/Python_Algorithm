import sys

sys.stdin = open("./input9.txt", "r")

N = int(input())
lst = list(map(int, input().split()))
string = ''
current = float("-Inf")

while True:
    if not lst:
        break

    l, r = lst[0] > current, lst[-1] > current
    if l and r:
        pop_idx = 0 if lst[0] <= lst[-1] else -1
        current = lst.pop(pop_idx)
        string += 'L' if pop_idx == 0 else 'R'
    elif l:
        current = lst.pop(0)
        string += 'L'
    elif r:
        current = lst.pop(-1)
        string += 'R'
    else:
        break

print(len(string))
print(string)
import sys

sys.stdin = open("./input4.txt", "r")

string = input()

nums = []
for e in string:
    if e.isdigit():
        nums.append(int(e))
    elif e == '+':
        res = nums.pop() + nums.pop()
        nums.append(res)
    elif e == '-':
        res = nums.pop() - nums.pop()
        nums.append(-res)
    elif e == '*':
        res = nums.pop() * nums.pop()
        nums.append(res)
    elif e == '/':
        res = nums.pop() * nums.pop()
        nums.append(1 / res)

print(*nums)

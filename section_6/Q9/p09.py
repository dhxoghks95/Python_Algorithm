import sys

sys.stdin = open("./input9.txt", 'r')

num, final = list(map(int, input().split()))
s = list(range(1, num+1))
res = []

coefs = [1] * num
for i in range(1, len(coefs)):
    coefs[i] = int(coefs[i-1] * (num-i) / i)


def permute(new_s):
    global res
    if len(new_s) == num:
        res.append(new_s[:])
        return
    else:
        for i in range(len(s)):
            if s[i] not in new_s:
                new_s.append(s[i])
                permute(new_s)
                new_s.pop()


permute([])

for g in res:
    if sum(map(lambda x, y: x*y, g, coefs)) == final:
        print(*g)
        break
        
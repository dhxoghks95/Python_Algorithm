import sys

sys.stdin = open("./input4.txt", 'r')

N = int(input())
s = list(map(int, input().split()))


def subset_even(s):
    if sum(s) % 2 != 0:
        return False
    else:
        include = [False for _ in range(len(s))]
        num = sum(s) / 2
        flag = False

        def subset(idx):
            nonlocal flag
            if idx == len(s):
                lst = []
                for i in range(len(s)):
                    if include[i]:
                        lst.append(s[i])
                if sum(lst) == num:
                    flag = True
                return
            include[idx] = True
            if not flag:
                subset(idx + 1)
            if not flag:
                include[idx] = False
                subset(idx + 1)

        subset(0)
        return flag


flag = subset_even(s)
print("YES" if flag else "NO")

import sys

sys.stdin = open("./input3.txt", "r")

string = input()

operators = []
res = ''
priority = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2}
for e in string:
    if e.isdigit():
        res += e
    else:
        if e == '(':
            operators.append(e)
        elif e == ')':
            while True:
                tmp = operators.pop()
                if tmp == '(':
                    break
                else:
                    res += tmp
        else:
            if len(operators) == 0:
                operators.append(e)
            else:
                if priority[e] > priority[operators[-1]]:
                    operators.append(e)
                else:
                    res += operators.pop()
                    operators.append(e)

while len(operators) > 0:
    res += operators.pop()

print(res)

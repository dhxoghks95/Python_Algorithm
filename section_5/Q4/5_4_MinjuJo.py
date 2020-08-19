import sys
sys.stdin = open("in5.txt", "r")

postfix = list(input())
num = []

for pos in postfix:
    if pos.isdigit():
        num.append(pos)
    else:
        num1, num2 = int(num.pop()), int(num.pop())
        if pos == "+":
            num.append(num2 + num1)
        elif pos == "-":
            num.append(num2 - num1)
        elif pos == "*":
            num.append(num2 * num1)
        else: # pos == "/"
            num.append(num2 / num1)

print(num[0])

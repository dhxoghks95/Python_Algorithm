import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/4. 후위식 연산/in1.txt","rt")

sick = input()
stack = []
for i in sick:
    if i.isdecimal():
        stack.append(int(i))
    else:
        if i == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)
        elif i == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif i == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif i == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)

print(stack[0])
"""
Section 5 - Q3

후위표기식 만들기
"""

import sys
sys.stdin = open('input.txt', 'r')
equation = input() # 중위표기식
res = '' # 정답 (후위표기식)

stack = [] # 연산자 순서 처리할 스택
for x in equation:
    if x.isdecimal(): # 숫자인 경우
        res += x
    else: # 연산자인 경우
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'): # 스택 상단이 x보다 연산 우선순위가 높으면
                res += stack.pop() # x보다 연산 우선순위 높은 것들을 스택에서 꺼내서 정답에 넣어줌
            stack.append(x) # x를 스택에 넣어줌
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(': # 스택 상단이 x보다 연산 우선순위가 높으면 (괄호 속 연산자가 아닐 때)
                res += stack.pop() # x보다 연산 우선순위 높은 것들을 스택에서 꺼내서 정답에 넣어줌
            stack.append(x) # x를 스택에 넣어줌
        elif x==')':
            while stack and stack[-1]!='(': # 스택 상단이 (가 아니면 즉 (를 만날 때까지
                res += stack.pop() # 스택에서 연산자를 꺼내서 정답에 넣어줌
            stack.pop() # 스택에서 ( 제거

# 스택에 연산자가 남아있는 경우
while stack:
    res += stack.pop() # 순차적으로 뒤에 붙임

# 정답 출력
print(res)
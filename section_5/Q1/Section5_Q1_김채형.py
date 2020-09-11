"""
Section 5 - Q1

가장 큰수

선생님은 현수에게 숫자 하나를 주고,
해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들라고 했습니다.
여러분이 현수를 도와주세요.(단 숫자의 순서는 유지해야 합니다)
만약 5276823 이 주어지고 3개의 자릿수를 제거한다면
7823이 가장 큰 숫자가 됩니다.
"""

import sys
sys.stdin = open("input.txt", "rt")

number, m = map(int, input().split())
number = list(map(int, str(number)))

stack = []
for x in number:
    while stack and m>0 and stack[-1]<x: # 스택에 last로 들어간 숫자가 이제 들어가고자 하는 x보다 작으면
        stack.pop() # 스택 last out
        m -= 1 # 한개 제거했으므로 -1
    stack.append(x)

# 스택에서 m개만큼 제거하지 않았을 때
if m!=0:
    stack = stack[:-m] # 맨 뒤쪽 m개 제거

res = ''.join(map(str, stack))
print(res)
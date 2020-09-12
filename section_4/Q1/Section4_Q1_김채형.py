"""
Section 4 - Q1

이분검색

임의의 N개의 숫자가 입력으로 주어집니다.
N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면
이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요.
단 중복값은 존재하지 않습니다.
"""

import sys
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split(' '))
ls = list(map(int, input().split(' ')))
ls.sort()

lt = 0 # 왼쪽 인덱스
rt = n-1 # 오른쪽 인덱스
while lt <= rt:
    mid = (lt+rt)//2 # 가운데 인덱스
    if ls[mid] > m: # 우리가 찍은 값이 원하는 값보다 오른쪽에 있으면
        rt = mid-1 # rt를 업데이트 해서 왼쪽을 검색하도록 함
    elif ls[mid] < m: # 우리가 찍은 값이 원하는 값보다 왼쪽에 있으면
        lt = mid+1 # lt를 업데이트 해서 오른쪽을 검색하도록 함
    else: # 우리가 찍은 값이 원하는 값이면
        print(mid+1) # 출력
        break

"""   
import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split(' '))
ls = list(map(int, input().split(' ')))
ls.sort()
for idx, scalar in enumerate(ls):
    if scalar == m:
        print(idx+1)
"""
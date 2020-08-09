"""
Section 2 - Q4

대표값

N명의 학생의 수학성적이 주어집니다.
N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
답이 2개일 경우 성적이 높은 학생의 번호를 출력하세요. 만약 답이 되는 점수가 여러 개일 경우 번호가 빠른 학생의 번호를 답으로 한다.
"""

import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
score_ls = list(map(int, input().split()))

score_mean = round(sum(score_ls) / n, 1)

minimum = abs(score_ls[0] - score_mean)
student_score = 0
for idx, x in enumerate(score_ls):
    diff = abs(x - score_mean)
    if diff < minimum:
        student_id = idx
        student_score = x
    elif diff == minimum:
        if x > student_score:
            student_id = idx
            student_score = x

print(score_mean, student_id)
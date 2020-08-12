import sys
sys.stdin = open('input.txt','r')

n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()

#어차피 2명 밖에 못 태우니까...
m_raw = m # 원본값 보존
lt = 0
rt = n-1
cnt = 0

while lt <= rt:
    m -= weight[lt] #남은 사람 중 가장 마른 사람을 태워본다.
    if m < weight[rt]: #남은 사람 중 가장 뚱뚱한 사람이 너무 뚱뚱하면
        rt -= 1 #뚱뚱한 사람 혼자
        cnt += 1 #태운다
        m = m_raw #초기화
    elif m >= weight[rt]: #남은 사람 중 가장 뚱뚱한 사람이 충분히 말랐으면
        lt += 1 #같이(마른이)
        rt -= 1 #같이(뚱뚱이)
        cnt += 1 #태운다.
        m = m_raw #초기화
print(cnt)

# input 예시
# 50, 60, 70, 90, 100
#####################
# lt    rt  m   cnt
# 0	    4	140	0
# 0	    3	90	1
# 0	    3	140	1
# 1	    2	90	2
# 1	    2	140	2
# 2	    1	80	3

import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/4. 대표값/in1.txt", "rt")

n = int(input())
print(n)
a = list(map(int, input().split()))

avg = round(sum(a)/n, 0)

error_old = avg
answer = 0
error_cnt = 0
for i in range(n):
    error_new = abs(avg - a[i])
    if error_new < error_old:
        error_old = error_new
        answer = a[i]
        error_cnt = i+1
    if error_new == error_old:
        if a[i] > answer:
            answer = a[i]
            error_old = error_new
            error_cnt = i+1

print(avg, error_cnt)

        


    
    


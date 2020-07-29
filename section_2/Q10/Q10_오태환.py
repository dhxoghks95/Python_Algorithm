import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/10. 점수 계산/in1.txt","rt")

n = int(input())
a = list(map(int, input().split()))

a
score = 0
b = a.copy()
for i in range(n, 0 , -1):
  
    maxnum = n - i + 1
    
    for j in range(maxnum):
       if sum(b[j:j+i]) == i:
          score = score +  sum(list(range(1,i+1)))
          
          for m in range(j, j+i+1):
            b[m] = 0
            


print(score)



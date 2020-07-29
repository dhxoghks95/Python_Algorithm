import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/3. k번째 큰 수/in1.txt", 'rt')

n, k = map(int, input().split())
a = list(map(int, input().split()))



total = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            total.add(a[i] + a[j] + a[m] )
total = list(total)
total.sort(reverse = True)
print(total[k-1])
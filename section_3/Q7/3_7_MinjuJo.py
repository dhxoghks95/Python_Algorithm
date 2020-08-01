import sys
sys.stdin = open("in5.txt", "r")

num = int(input())
matrix = []
for _ in range(num) :
    matrix.append(list(map(int, input().split())))

apple_sum = 0
middle = (num//2) + 1

for i in range(middle):
    apple_sum += sum(matrix[i][middle - (i+1) : middle + i])
    if (middle - (i+1)) == 0:
        break
    apple_sum += sum(matrix[num - i- 1][middle - (i+1) : middle + i])

print(apple_sum)
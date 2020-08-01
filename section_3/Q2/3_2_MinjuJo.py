import sys
sys.stdin = open("in5.txt", "r")

word = input()
digit_num = 0
num = 0 # number we want

for letter in word[::-1]:
    if letter.isdigit():
        num += int(letter) * (10 ** digit_num)
        digit_num += 1

divisor_cnt = 0
for i in range(1,round((num+1)**0.5)):
    if num % i == 0:
        if num // i == i:
            divisor_cnt += 1
        else:
            divisor_cnt += 2

print(num)
print(divisor_cnt)
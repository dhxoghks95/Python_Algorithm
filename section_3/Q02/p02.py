digits = list(filter(lambda x: x.isdigit(), input()))
digits = digits[1:] if digits[0] == '0' else digits

num = int(''.join(digits))
cnt = 2 # 1과 자기자신

for i in range(2, int(num/2)+1):
    if num % i == 0:
        cnt +=1

print(num)
print(cnt)
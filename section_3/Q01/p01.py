N = int(input("N 입력: "))

lst = []
for i in range(1, N+1):
    word = input().lower()
    lst.append(f"#{i} YES" if word == word[::-1] else f"#{i} NO")

print(*lst, sep='\n')
lst = []

N = int(input("N 입력: "))
lst.extend(input().split())

M = int(input("M 입력: "))
lst.extend(input().split())

lst.sort()
print(*lst)
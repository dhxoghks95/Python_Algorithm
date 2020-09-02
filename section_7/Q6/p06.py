import sys

sys.stdin = open('./input6.txt', 'r')

encrypted = input()
CODES = tuple(map(str.upper, 'abcdefghijklmnopqrstuvwxyz'))
cnt = 0


def decrypt(start, end, string):
    global cnt
    if start >= len(encrypted) and end-start == 1:
        print(string)
        cnt += 1

    if end > len(encrypted):
        return

    num = int(encrypted[start:end])
    if num not in range(1, 27):
        return

    tmp = CODES[num-1]
    string += tmp

    # 예외처리
    if encrypted[start:end][0] != '0':
        decrypt(end, end+1, string)
        decrypt(end, end+2, string)


decrypt(0, 1, '')
decrypt(0, 2, '')
print(cnt)

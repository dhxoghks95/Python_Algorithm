import sys
sys.stdin = open("in5.txt", "r")
n = int(input())

for i in range(n):
    word = input()
    word = word.lower()
    if word == word[::-1]:
        print("#%d YES"%(i))
    else:
        print("#%d NO"%(i))
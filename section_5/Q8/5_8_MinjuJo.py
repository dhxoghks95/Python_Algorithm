import sys
sys.stdin = open("in5.txt", "r")

vocab_num = int(input())
vocabs = []
for _ in range(vocab_num):
    vocabs.append(input())

for _ in range(vocab_num - 1):
    vocabs.remove(input())

print(vocabs[0])
import sys
sys.stdin = open("in5.txt", "r")

word1, word2 = list(input()), list(input())
ana = "YES"

for word in word1:
    try:
        word2.remove(word)
    except:
        ana = "NO"
        break

if (ana == "YES") & (len(word2) != 0):
    ana = "NO"

print(ana)
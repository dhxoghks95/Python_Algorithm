import sys

sys.stdin = open("./input9.txt", "r")

word1 = input().lower()
word2 = input().lower()

word1_dict = {}
word2_dict = {}

for word in word1:
    if word in word1_dict:
        word1_dict[word] += 1
    else:
        word1_dict[word] = 1

for word in word2:
    if word in word2_dict:
        word2_dict[word] += 1
    else:
        word2_dict[word] = 1

flag = True
for word in word1:
    if word1_dict[word] != word2_dict[word]:
        flag = False
        break

print("YES" if flag else "NO")

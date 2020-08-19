import sys
sys.stdin = open("in5.txt", "r")

cuts = input()
current_stack = []
laser = False
count = 0

for i in range(len(cuts)):
    if laser:
        laser = False
        continue

    if cuts[i] == "(":
        if cuts[i+1] == ")":
            laser = True
            count += len(current_stack)
        else:
            current_stack.append(cuts[i]) # current_num += 1
    else:
        current_stack.pop() #current_num -= 1
        count += 1

print(count)

import sys
sys.stdin = open("in5.txt", "r")

cals = input()
buho, postfix = [], ""

def get_order(cal):
    if cal in ["*", "/"]:
        return 1
    elif cal in ["+", "-"]:
        return 2
    else:
        return 3

for cal in cals:
    if cal.isdigit():
        postfix += cal
    else:
        if cal == "(" or (len(buho) == 0):
            buho.append(cal)
        elif cal == ")":
            while buho[-1] != "(":
                postfix += buho.pop()
            buho.pop()
        else:
            if get_order(cal) < get_order(buho[-1]):
                buho.append(cal)
            else: # if order is same or higher (order 1 is higher than order 2)
                while ((len(buho) > 0) and (get_order(cal) >= get_order(buho[-1]))):
                    postfix += buho.pop()
                buho.append(cal)

while len(buho) > 0:
    postfix += buho.pop()

print(postfix)
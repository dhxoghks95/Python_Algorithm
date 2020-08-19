import sys
sys.stdin = open("in5.txt", "r")

order = list(input())
class_num = int(input())

for i in range(class_num):
    clss = list(input())
    order_lst = list(order)
    right = "YES"

    for cls in clss:
        if cls in order_lst:
            if order_lst[0] != cls:
                right = "NO"
                break
            else:
                order_lst.remove(cls)
    if len(order_lst) != 0:
        right = "NO"

    print("#{}".format(i+1), right)


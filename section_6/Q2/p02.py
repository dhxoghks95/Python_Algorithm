# 전위순회
tree = [0, 1, 2, 3, 4, 5, 6, 7]
start = 0
root = 1
cnt = 0

while cnt < len(tree)-1:
    if start == 0:
        if root*2 < len(tree):
            cnt += 1
            print(tree[root])
            root *= 2
        elif 2*(root//2)+1 < len(tree):
            cnt += 1
            print(tree[root])
            root = 2*(root//2)+1
            cnt += 1
            print(tree[root])
            start += 1
    else:
        if start == 1:
            root = start*2+1
        if root * 2 < len(tree):
            cnt += 1
            print(tree[root])
            root *= 2
        elif 2 * (root // 2) + 1 < len(tree):
            cnt += 1
            print(tree[root])
            cnt += 1
            root = 2 * (root // 2) + 1
            print(tree[root])
        start += 1

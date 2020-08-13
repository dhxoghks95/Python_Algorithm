import sys

sys.stdin = open("./input1.txt", "r")

N, K = list(map(int, input().split()))
lst = list(map(int, input().split()))
lst.sort()


def binary_search(arr, low, high, *, key):
    mid = int((low + high) / 2)
    if arr[mid] == key:
        return mid+1
    elif arr[mid] > key:
        res = binary_search(arr, low=low, high=mid-1, key=key)
    else:
        res = binary_search(arr, low=mid+1, high=high, key=key)

    return res


print(binary_search(lst, 0, N-1, key=K))

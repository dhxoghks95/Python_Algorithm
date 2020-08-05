import sys
sys.stdin = open("in5.txt", "r")

house_num, horse_num = map(int, input().split())
house_coor = sorted([int(input()) for _ in range(house_num)])
interval_lst = list(range(house_coor[-1] - house_coor[0] + 1))

def count_available_horses(interval, house_coor):
    horse_count = 0
    for house in house_coor:
        if horse_count == 0:
            prev = house
            horse_count +=1
        else:
            if (house - prev) >= interval:
                horse_count += 1
                prev = house
    return horse_count

left = 0
right = len(interval_lst) - 1
last_interval = 1
found = False

while not found:
    int_idx = (left + right) // 2
    available_horses = count_available_horses(interval_lst[int_idx], house_coor)

    if available_horses >= horse_num:
        left = int_idx + 1
        last_interval = interval_lst[int_idx]
    else:
        right = int_idx - 1

    if left > right:
        found = True

print(last_interval)
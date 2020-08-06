import sys
sys.stdin = open("in5.txt", "r")

song_num, disc_num = map(int, input().split())
songs = list(map(int, input().split()))
search_tree = list(range(sum(songs)))

def count_available_cds(songs_lst, cd_cap_idx, search_tree):
    cd_num = 0
    song_sum = 0
    cd_cap = search_tree[cd_cap_idx]
    for song in songs_lst:
        song_sum += song
        if song_sum > cd_cap:
            cd_num += 1
            song_sum = song
    return cd_num

found = False
left = 0
right = len(search_tree) - 1

while not found:
    cd_cap_idx = (left + right) // 2
    counted_cd_num = count_available_cds(songs, cd_cap_idx, search_tree)

    if counted_cd_num >= disc_num:
        cd_cap = search_tree[cd_cap_idx]
        left = cd_cap_idx + 1

    else:
        right = cd_cap_idx - 1

    if left > right:
        found = True

print(cd_cap + 1)
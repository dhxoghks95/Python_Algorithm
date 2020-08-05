import sys
sys.stdin = open("in5.txt", "r")

num = int(input())
timetable = []
for _ in range(num):
    start, end = map(int, input().split())
    timetable.append((start, end))

timetable = sorted(timetable, key = lambda time : (time[1], time[0]))
cnt = 1 # at least one meeting
end = timetable[0][1] # first end value

for i in range(1, num): # except the first meeting
    if end <= timetable[i][0]:
        cnt += 1
        end = timetable[i][1]

print(cnt)
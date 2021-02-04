from sys import stdin
input = stdin.readline

meetings = []
for _ in range(int(input())):
    meeting = tuple(map(int,input().split()))
    meetings.append(meeting)
meetings.sort(key=lambda meeting: meeting[0])
meetings.sort(key=lambda meeting: meeting[1])

count, lastEnd = 0, 0
for meeting in meetings:
    if meeting[0] >= lastEnd:
        count += 1
        lastEnd = meeting[1]

print(count)
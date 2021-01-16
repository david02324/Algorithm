count = int(input())
k = []
n = []
for _ in range(count):
    k.append(int(input()))
    n.append(int(input()))

room = [[0 for roomNum in range(max(n)+1)] for floor in range(max(k)+1)]
for i in range(max(n)+1):
    room[0][i] = i

for floor in range(1,max(k)+1):
    for roomNum in range(1,max(n)+1):
        room[floor][roomNum] = room[floor-1][roomNum] + room[floor][roomNum-1]

for result in range(count):
    print(room[k[result]][n[result]])
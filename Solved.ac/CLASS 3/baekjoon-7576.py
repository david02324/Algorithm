# dawitblog.tistory.com
from sys import stdin
from collections import deque


dx = [0,0,1,-1]
dy = [1,-1,0,0]
def tomato_bfs(box,queue):
    global changed
    while queue:
        tx,ty = queue.popleft()

        for i in range(4):
            x = tx + dx[i]
            y = ty + dy[i]

            if 0<= x < c and 0<= y < r:
                if box[y][x] == 0 or box[ty][tx] + 1 < box[y][x]:
                    changed = True
                    box[y][x] = box[ty][tx] + 1
                    queue.append((x,y))


c, r = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(r)]

# 익지 않은 토마토가 하나라도 있는지 확인
anyRawTomato = False
queue = deque([])
for y in range(r):
    for x in range(c):
        if box[y][x] == 1:
            queue.append((x,y))
        elif box[y][x] == 0:
            anyRawTomato = True

# bfs
tomato_bfs(box,queue)

# 처음에 모두 익은 토마토였다면
if not anyRawTomato:
    print(0)
else:
    maxDay = 0
    for y in range(r):
        for x in range(c):
            if not box[y][x]:
                print(-1)
                exit()
            maxDay = max(maxDay,box[y][x])
    print(maxDay-1)
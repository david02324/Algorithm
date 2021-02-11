# dawitblog.tistory.com
from sys import stdin
from collections import deque
input = stdin.readline

def tomato_bfs(boxes,queue):
    global changed
    dx = [0,0,0,0,1,-1]
    dy = [0,0,1,-1,0,0]
    dz = [1,-1,0,0,0,0]

    while queue:
        tx,ty,tz = queue.popleft()
        for i in range(6):
            newX = tx + dx[i]
            newY = ty + dy[i]
            newZ = tz + dz[i]

            # 상자를 벗어나지 않는다면
            if 0<=newX<c and 0<=newY<r and 0<=newZ<h:
                if boxes[newZ][newY][newX] == 0 or boxes[tz][ty][tx]+1<boxes[newZ][newY][newX]:
                    # 한번이라도 새로 익은 토마토가 있는지 확인
                    changed = True
                    boxes[newZ][newY][newX] = boxes[tz][ty][tx]+1
                    queue.append((newX,newY,newZ))

c,r,h = map(int,input().split())
boxes = [[list(map(int,input().split())) for _ in range(r)] for _ in range(h)]

anyRawTomato = False 
queue = deque([])
for z in range(h):
    for y in range(r):
        for x in range(c):
            # 처음부터 익어있던 토마토를 만났을 경우
            if boxes[z][y][x] == 1:
                queue.append((x,y,z))
            elif boxes[z][y][x] == 0:
                # 초기에 날것의 토마토가 하나라도 있다면
                anyRawTomato = True

# bfs
tomato_bfs(boxes,queue)

# 처음에 모두 다 익은 토마토였다면
if not anyRawTomato:
    print(0)
else:
    maxDay = 0
    # 안익은 토마토가 하나라도 있는지 확인
    for z in range(h):
        for y in range(r):
            for x in range(c):
                if not boxes[z][y][x]:
                    print(-1)
                    exit()
                maxDay = max(maxDay,boxes[z][y][x])

    # 가장 오래 걸리는 시간 출력
    print(maxDay-1)
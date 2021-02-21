# dawitblog.tistory.com/111
from sys import stdin
input = stdin.readline
from collections import deque

# 초기 상어 크기, 스택, 시간
shark,sharkStack,time = 2,0,0
dr = [-1,0,0,1]
dc = [0,-1,1,0]
def eatOne(sr,sc):
    global shark,sharkStack,time

    visited = [[False]*n for _ in range(n)]
    queue = deque([(sr,sc,0)])
    minDistance = 1e9
    # 한 마리라도 먹을 수 있는지 확인
    eat = False
    while queue:
        tr, tc, d = queue.popleft()
        # 만약 먹을 수 있는 물고기가 있다면
        if space[tr][tc] and space[tr][tc] < shark:
            # 첫 발견일 시
            if d < minDistance:
                visited[tr][tc] = True
                minDistance = d
                eatables = [(tr,tc)]
                eat = True
            # 두 번째 이후일 시
            elif d == minDistance:
                eatables.append((tr,tc))
            
            continue
        
        # 지나갈 수 있고, 지나가지 않았다면
        if (not space[tr][tc] or space[tr][tc] == shark) and not visited[tr][tc]:
            visited[tr][tc] = True

            for i in range(4):
                newR, newC = tr + dr[i], tc + dc[i]

                if 0<=newR<n and 0<=newC<n:
                    queue.append((newR,newC,d+1))

    # 물고기를 먹었다면
    if eat:
        eatables.sort(key=lambda x: (x[0],x[1]))
        tr, tc = eatables[0]
        
        # 이동 시간 누적
        time += minDistance
        # 이동해서 물고기 먹기
        space[tr][tc] = 0

        # 상어 스택
        sharkStack += 1
        if sharkStack == shark:
            shark += 1
            sharkStack = 0

        # 이동 후 상어의 위치 반환
        return (tr,tc)
    # 먹지 못했다면
    else:
        return False

n = int(input())
space = []
for r in range(n):
    row = list(map(int,input().split()))
    for c in range(n):
        # 초기 상어의 위치 저장 후 0으로 변경
        if row[c] == 9:
            sr, sc = r, c
            row[c] = 0
    space.append(row)

while True:
    nextPos = eatOne(sr,sc)
    if nextPos:
        sr, sc = nextPos
    else:
        break

print(time)
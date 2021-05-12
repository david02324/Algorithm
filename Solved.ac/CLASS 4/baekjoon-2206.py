# dawitblog.tistory.com/156
from sys import stdin
from collections import deque
input = stdin.readline

R, C = map(int,input().split())
mat = [input().rstrip() for _ in range(R)]
# 방문 확인
visited = [[[0,0] for _ in range(C)] for _ in range(R)]
visited[0][0][0] = 1
# 큐
q = deque([(0,0,1,0)])
move = [(0,1),(1,0),(-1,0),(0,-1)]

while q:
    r,c,d,isWallBroken = q.popleft()
    # 목적지 도달시
    if r == R-1 and c == C-1:
        print(d)
        exit()

    for dr,dc in move:
        newR = r+dr
        newC = c+dc
        if 0<= newR < R and 0<= newC < C and not visited[newR][newC][isWallBroken]:
            # 벽이 아니라면
            if mat[newR][newC] == '0':
                visited[newR][newC][isWallBroken] = d+1
                q.append((newR,newC,d+1,isWallBroken))
            # 벽이지만 벽을 부순 적이 없다면
            elif not isWallBroken:
                visited[newR][newC][1] = d+1
                q.append((newR,newC,d+1,1))

print(-1)
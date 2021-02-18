# dawitblog.tistory.com
from sys import stdin
input = stdin.readline
from collections import deque

n = int(input())
mat = [input().rstrip() for _ in range(n)]
# G를 모두 R로 변경
mat2 = [s.replace('G','R') for s in mat]
dr = [0,0,1,-1]
dc = [1,-1,0,0]

# bfs
def bfs(mat,r,c,visited):
    rgb = mat[r][c]

    queue = deque([(r,c)])
    visited[r][c] = True

    while queue:
        tr, tc = queue.popleft()
        for i in range(4):
            newR = tr + dr[i]
            newC = tc + dc[i]

            if 0<=newR<n and 0<=newC<n and mat[newR][newC]==rgb and not visited[newR][newC]:
                visited[newR][newC] = True
                queue.append((newR,newC))

# 정상인이 보이는 구역
visited = [[False]*n for _ in range(n)]
count = 0
for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            bfs(mat,r,c,visited)
            count += 1

# 적록색약을 가진 사람이 보이는 구역
visited = [[False]*n for _ in range(n)]
rgbCount = 0
for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            bfs(mat2,r,c,visited)
            rgbCount += 1

print(count, rgbCount)
# dawitblog.tistory.com
from collections import deque
n, m = map(int,input().split())
# 미로 list
maze = [[]] + [[0] + list(map(int,list(input()))) for _ in range(n)]
case = []

visited = [[]] + [[False] * (m+1) for _ in range(n)]

visited[1][1] = True
queue = deque([(1,1,1)])
while queue:
    tr,tc,d = queue.popleft()
    if tr + 1 <= n and maze[tr+1][tc] and visited[tr+1][tc] is False:
        visited[tr+1][tc] = True
        if (tr+1,tc) == (n,m):
            print(d+1)
            exit()
        queue.append((tr+1,tc,d+1))
    if tc + 1 <= m and maze[tr][tc+1] and visited[tr][tc+1] is False:
        visited[tr][tc+1] = True
        if (tr,tc+1) == (n,m):
            print(d+1)
            exit()
        queue.append((tr,tc+1,d+1))
    if tr - 1 > 0 and maze[tr-1][tc] and visited[tr-1][tc] is False:
        visited[tr-1][tc] = True
        queue.append((tr-1,tc,d+1))
    if tc - 1 > 0 and maze[tr][tc-1] and visited[tr][tc-1] is False: 
        visited[tr][tc-1] = True
        queue.append((tr,tc-1,d+1))
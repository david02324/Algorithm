# dawitblog.tistory.com
import sys
from collections import deque
input = sys.stdin.readline

# 지도 list
m = [list(map(int,list(input().rstrip()))) for _ in range(int(input()))]

# 방문 확인 list
visited = [[False] * len(m) for _ in range(len(m))]

# 너비 우선 탐색
def bfs(m,r,c):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    visited[r][c] = True
    queue = deque([(r,c)])
    count = 1

    while queue:
        tr,tc = queue.popleft()
        for i in range(4):
            newR = tr + dr[i]
            newC = tc + dc[i]
            if 0 <= newR < len(m) and 0 <= newC < len(m) and m[newR][newC] and not visited[newR][newC]:
                visited[newR][newC] = True
                queue.append((newR,newC))
                count += 1
    
    return count

# 아파트 단지 수
aparts = 0
houses = []
for r in range(len(m)):
    for c in range(len(m)):
        if m[r][c] and visited[r][c] is False:
            aparts += 1
            houses.append(bfs(m,r,c))

print(aparts)
# 정렬 잊지말자.
print('\n'.join(map(str,sorted(houses))))
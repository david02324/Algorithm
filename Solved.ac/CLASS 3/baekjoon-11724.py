# dawitblog.tistory.com
from sys import stdin
from collections import deque

input = stdin.readline

n,m = map(int,input().split())

# 정점 저장
nodes = [[] for _ in range(n+1)]
# 방문 처리
visited = [False] * (n+1)
for _ in range(m):
    i,j = map(int,input().split())
    nodes[i].append(j)
    nodes[j].append(i)

# 너비 우선 탐색
def bfs(start):
    global nodes,visited
    if visited[start]:
        return 0

    visited[start] = True
    queue = deque([start])

    while queue:
        for node in nodes[queue.popleft()]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)

    return 1

# 깊이 우선 탐색
def dfs(start):
    global nodes,visited
    if visited[start]:
        return 0
    
    visited[start] = True
    stack = [start]

    if not nodes[stack[-1]]:
        return 1
    while stack:
        for idx,node in enumerate(nodes[stack[-1]]):
            if not visited[node]:
                visited[node] = True
                stack.append(node)
                break
            if idx == len(nodes[stack[-1]]) - 1:
                stack.pop()
    
    return 1

count = 0
for i in range(1,n+1):
    count += dfs(i)
print(count)
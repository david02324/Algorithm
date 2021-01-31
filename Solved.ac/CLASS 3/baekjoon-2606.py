import sys
from collections import deque
input = sys.stdin.readline

coms = [set() for _ in range(int(input())+1)]
for _ in range(int(input())):
    a, b = map(int,input().split())
    coms[a].add(b)
    coms[b].add(a)

def bfs(graph,root):
    queue = deque([root])

    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited = [False] * len(coms)
bfs(coms,1)
print(visited.count(True)-1)
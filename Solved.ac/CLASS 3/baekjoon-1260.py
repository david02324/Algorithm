import sys
from collections import deque
input = sys.stdin.readline

n,m,root = map(int,input().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    nodes[i].append(j)
    nodes[j].append(i)

for i in range(len(nodes)):
    nodes[i].sort()

def dfs(start,n):
    visited = [False] * (n+1)
    stack = []
    answerli = []

    visited[start] = True
    answerli.append(start)
    stack.append(start)
    # 시작 노드에 인접 노드가 하나도 없을 경우
    if not nodes[start]:
        return [start]

    while stack:
        for idx,node in enumerate(nodes[stack[-1]]):
            if not visited[node]:
                # 방문 처리
                visited[node] = True
                answerli.append(node)
                stack.append(node)
                break
            # 주변 노드가 모두 방문되었다면
            if idx == len(nodes[stack[-1]]) - 1:
                stack.pop()
    
    return answerli

def bfs(start,n):
    visited = [False] * (n+1)
    queue = deque()
    answerli = []

    visited[start] = True
    answerli.append(start)
    queue.append(start)
    while queue:
        for node in nodes[queue.popleft()]:
            if not visited[node]:
                # 방문 처리
                visited[node] = True
                answerli.append(node)
                queue.append(node)

    return answerli



print(' '.join(map(str,dfs(root,n))))
print(' '.join(map(str,bfs(root,n))))
# dawitblog.tistory.com/153
from sys import stdin,setrecursionlimit
input = stdin.readline
# 재귀깊이 설정
setrecursionlimit(10**9)

def dfs(node):
    global start_point
    for next_node,cost in nodes[node]:
        if not distances[next_node] and next_node != start_point: # 시작점은 0으로 유지
            distances[next_node] = distances[node] + cost
            dfs(next_node)


n = int(input())
nodes = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    nodes[a].append((b,c))
    nodes[b].append((a,c))

distances = [0] * (n+1)
# 임의의 점에서 시작
start_point = 1
# 가장 먼 노드 탐색
dfs(start_point)

max_dis = 0
point_one = -1
for i in range(1,n+1):
    if distances[i] > max_dis:
        max_dis = distances[i]
        point_one = i

distances = [0] * (n+1)
# 가장 먼 노드에서 가장 먼 노드 탐색
start_point = point_one
dfs(start_point)

print(max(distances))
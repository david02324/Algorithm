# dawitblog.tistory.com
from sys import stdin
import heapq
input = stdin.readline

# 입력
V, E = map(int,input().split())
nodes = [[] for _ in range(V+1)]
# 시작점
start = int(input())
for _ in range(E):
    u,v,w = map(int,input().split())
    nodes[u].append((v,w))

dist = [1e9] * (V+1)
dist[start] = 0

# 가장 가까운 노드를 찾기 위한 힙
queue = []
heapq.heappush(queue,(0,start))

while queue:
    d, now = heapq.heappop(queue)
    # 이미 더 가까운 경로를 찾았다면 넘김
    if dist[now] < d:
        continue
    for dest, w in nodes[now]:
        cost = d + w
        # 더 가까운 경로를 찾았다면
        if cost < dist[dest]:
            dist[dest] = cost
            heapq.heappush(queue,(cost,dest))

# 출력
print('\n'.join([str(i) if i != 1e9 else 'INF' for i in dist[1:]]))
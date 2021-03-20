# dawitblog.tistory.com
from sys import stdin
input = stdin.readline
import heapq

l = int(input())
# 연결 정보를 저장할 리스트
nodes = [[] for _ in range(l+1)]
# 연결 정보 저장
for _ in range(int(input())):
    n,m,c = map(int,input().split())

    nodes[n].append((m,c))


start, end = map(int,input().split())
# 각 노드로 갈때 드는 최소비용
dist = [1e9] * (l+1)
dist[start] = 0

queue = []
heapq.heappush(queue,(0,start))

# Dijkstra
while queue:
    c1, now = heapq.heappop(queue)
    if dist[now] < c1:
        continue
    for dest,c2 in nodes[now]:
        cost = c1 + c2
        if cost < dist[dest]:
            dist[dest] = cost
            heapq.heappush(queue,(cost,dest))

# 출력
print(dist[end])
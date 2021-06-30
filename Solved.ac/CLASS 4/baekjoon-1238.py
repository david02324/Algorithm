# dawitblog.tistory.com/169
import sys
from heapq import heappop,heappush
input = sys.stdin.readline
INF = sys.maxsize

# 입력
n,m,x = map(int,input().split())
x -= 1
# 길 소요시간 리스트
roads = [[] for _ in range(n)]
# 역방향 리스트
rev_roads = [[] for _ in range(n)]

for _ in range(m):
    a,b,t = map(int,input().split())
    a -= 1
    b -= 1

    roads[a].append((b,t))
    rev_roads[b].append((a,t))

# 다익스트라
def dijkstra(graph , start, distance):
    hq = []
    heappush(hq,(0,start))
    distance[start] = 0

    while hq:
        dist , now = heappop(hq)

        if distance[now] < dist:
            continue

        for new in graph[now]:
            cost = dist + new[1]

            if cost < distance[new[0]]:
                distance[new[0]] = cost
                heappush(hq,(cost,new[0]))

    return distance

# x부터 다른 마을로 가는 최단거리
x_other = dijkstra(roads,x,[INF]*n)
# 각 마을에서 x로 가는 최단거리(역방향 그래프 이용)
other_x = dijkstra(rev_roads,x,[INF]*n)

# 출력
print(max([x_other[i] + other_x[i] for i in range(n) if i != x]))
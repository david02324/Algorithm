# dawitblog.tistory.com/166
import sys
from heapq import heappush,heappop
input = sys.stdin.readline
INF = sys.maxsize

# 다익스트라
def dijkstra(start, distance):
    hq = []
    heappush(hq,(0,start))
    distance[start] = 0

    while hq:
        dist , now = heappop(hq)

        if distance[now] < dist:
            continue

        for new in roads[now]:
            cost = dist + new[1]

            if cost < distance[new[0]]:
                distance[new[0]] = cost
                heappush(hq,(cost,new[0]))

    return distance

# 입력
n,m,r = map(int,input().split())
items = list(map(int,input().split()))
roads = [[] for _ in range(n)]
for _ in range(r):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1

    roads[a].append((b,c))
    roads[b].append((a,c))

# 각 지점에서 얻을 수 있는 아이템
max_items = 0
for start in range(n):
    item = 0
    for dest,dist in enumerate(dijkstra(start,[INF]*n)):
        if dist <= m:
            item += items[dest]
    
    max_items = max(max_items,item)

# 출력
print(max_items)
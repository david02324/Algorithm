# dawitblog.tistory.com/150
from heapq import heappop,heappush
from sys import stdin
input = stdin.readline
INF = 1e9

n, m = map(int,input().split())
nodes = [[] for i in range(n+1)]
for _ in range(m):
    a, b, d = map(int,input().split())
    nodes[a].append((b,d))
    nodes[b].append((a,d))
# 경유지
s1, s2 = map(int,input().split())

# 간선 없을 시
if m == 0:
    print(-1)
    exit()

# 다익스트라. end 지점까지의 최단거리 확정시 바로 종료
def find(start,end,nodes):
    q = []
    heappush(q,(0,start))
    distance = [INF]*(n+1)
    distance[start] = 0
    while True:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in nodes[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q,(cost,i[0]))
        if now == end:
            break
    return distance[end]

# s1과 s2까지의 최단경로를 각각 저장
q = []
heappush(q,(0,1))
distance = [INF]*(n+1)
distance[1] = 0
count = 0
while True:
    dist, now = heappop(q)
    if distance[now] < dist:
        continue
    if now == s1:
        count += 1
    if now == s2:
        count += 1
    for i in nodes[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heappush(q,(cost,i[0]))
    if count == 2:
        break

# d1 = 1->s1 , d2 = 1->s2
d1 = distance[s1]
d2 = distance[s2]

# b = s1->s2 , a1 = s1->n , a2 = s2->n
b = find(s1,s2,nodes)
a1 = find(s1,n,nodes)
a2 = find(s2,n,nodes)

# 출력
ans = min(d1+b+a2,d2+b+a1)
print(ans) if ans != 1e9 else print(-1)
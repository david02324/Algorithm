# dawitblog.tistory.com/165
from sys import stdin
input = stdin.readline

INF = 10_000_000
# 도시 수
n = int(input())

# 노선 비용 정보
cities = [[INF]*n for _ in range(n)]

# 입력
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1

    cities[a][b] = min(cities[a][b],c)

# 플로이드-와샬
for v in range(n):
    for a in range(n):
        for b in range(n):
            if a != b:
                cities[a][b] = min(cities[a][b],cities[a][v] + cities[v][b])

# 출력
for city in cities:
    print(*[i if i != INF else 0 for i in city])
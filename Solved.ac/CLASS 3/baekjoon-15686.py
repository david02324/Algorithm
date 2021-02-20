# dawitblog.tistory.com/109
from itertools import combinations
from sys import stdin
input = stdin.readline
from collections import deque

n, m = map(int,input().split())
city = [input().split() for _ in range(n)]

# 치킨집과 가정집 좌표 저장
chickens = []
houses = []
for r in range(n):
    for c in range(n):
        if city[r][c] == '2':
            chickens.append((r,c))
        elif city[r][c] == '1':
            houses.append((r,c))

# 치킨집을 남길 수 있는 조합
comb = list(combinations(chickens,m))
minCD = 1e9

dr = [0,0,1,-1]
dc = [1,-1,0,0]
# 케이스 마다 도시의 치킨 거리를 계산
for case in comb:
    cd = 0
    for house in houses:
        temp = 1e9
        for chicken in case:
            temp = min(temp,abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))
        cd += temp

    minCD = min(minCD,cd)

print(minCD)
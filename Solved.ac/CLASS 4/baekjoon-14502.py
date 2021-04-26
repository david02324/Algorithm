# dawitblog.tistory.com
from sys import stdin
from collections import deque
from copy import deepcopy
from itertools import combinations
input = stdin.readline

# 4방향 이동
move = [(1,0),(-1,0),(0,1),(0,-1)]

# BFS
def find(newWalls):
    global maxSafe
    # 큐 선언 후 바이러스 초기 위치로 초기화
    q = deque(virus)
    # 임시 리스트 복사
    copyMat = deepcopy(mat)

    # 벽 세우기
    for wallR,wallC in newWalls:
        copyMat[wallR][wallC] = 1

    while q:
        # 바이러스 좌표
        vr, vc = q.popleft()

        for dr,dc in move:
            # 추가되는 바이러스 좌표
            nr = vr + dr
            nc = vc + dc

            if 0<= nr < R and 0<= nc < C and not copyMat[nr][nc]:
                copyMat[nr][nc] = 2
                q.append((nr,nc))

    # 남아있는 안전구역 확인
    safe = 0
    for r in range(R):
        for c in range(C):
            if not copyMat[r][c]:
                safe += 1

    # 최고기록 갱신
    if safe > maxSafe:
        maxSafe = safe

    

R,C = map(int,input().split())
mat = []
virus = []
space = []
for r in range(R):
    l = list(map(int,input().split()))
    # 초기 바이러스,빈 공간 위치 기억
    for c in range(C):
        if l[c] == 2:
            virus.append((r,c))
        elif l[c] == 0:
            space.append((r,c))
    mat.append(l)

maxSafe = 0
# 벽 새울 곳 조합으로 구하기
newWalls = list(combinations(space,3))
for newWall in newWalls:
    find(newWall)
# 출력
print(maxSafe)
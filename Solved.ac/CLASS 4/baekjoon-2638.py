# dawitblog.tistory.com/158
from sys import stdin
from collections import deque
input = stdin.readline

R,C = map(int,input().split())
mat = []
for _ in range(R):
    mat.append(list(map(int,input().split())))

time = 0
moves = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(startPoints):
    q = deque(startPoints)
    while q:
        nowR,nowC = q.popleft()
        visited[nowR][nowC] = True
        for dr,dc in moves:
            newR = nowR + dr
            newC = nowC + dc

            if 0<=newR<R and 0<=newC<C and not mat[newR][newC] and not visited[newR][newC]:
                visited[newR][newC] = True
                q.append((newR,newC))

# 방문 리스트
visited = [[False]*C for _ in range(R)]
bfs([(0,0)])

while True:
    # 없어질 치즈 리스트
    cl = []
    for r in range(R):
        for c in range(C):
            if mat[r][c]:
                count = 0
                # 4가지 방향 중에서 외부와 접촉한 가짓수 확인
                for dr,dc in moves:
                    newR = r + dr
                    newC = c + dc

                    if visited[newR][newC]:
                        count += 1
                
                if count >= 2:
                    cl.append((r,c))

    if cl:
        for cheese in cl:
            r,c = cheese
            mat[r][c] = 0
        time += 1
    else:
        break
    # 없어진 치즈부터 bfs 수행
    bfs(cl)

print(time)
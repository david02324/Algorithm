# dawitblog.tistory.com
from sys import stdin
input = stdin.readline

r,c = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(r)]

maxValue = max(max(mat))

visited = [[False]*c for _ in range(r)]
drc = [(1, 0), (0, -1), (-1, 0), (0, 1)]
# DFS
def dfs(k,s,tr,tc):
    global realMax

    # 나머지를 모두 최대값만 더했을때도 이미 저장된 값보다 작다면
    if s + maxValue*(3-k) <= realMax:
        return
    if k == 3:
        realMax = max(realMax,s)
        return

    for dr,dc in drc:
        newR = tr + dr
        newC = tc + dc

        if 0<=newR<r and 0<=newC<c and not visited[newR][newC]:
            if k == 1:
                visited[newR][newC] = True
                dfs(k+1,s+mat[newR][newC],tr,tc)
                visited[newR][newC] = False
            
            visited[newR][newC] = True
            dfs(k+1,s+mat[newR][newC],newR,newC)
            visited[newR][newC] = False

realMax = 0
for R in range(r):
    for C in range(c):
        visited[R][C] = True
        dfs(0,mat[R][C],R,C)
        visited[R][C] = False

print(realMax)
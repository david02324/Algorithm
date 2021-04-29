# dawitblog.tistory.com/147
from sys import stdin
input = stdin.readline

R,C,T = map(int,input().split())
# 미세먼지 정보
mat = []
# 공기청정기 위치
cl = []
# 확산 방향
move = [(0,1),(0,-1),(1,0),(-1,0)]

for r in range(R):
    l = list(map(int,input().split()))
    if l[0] == -1:
        cl.append(r)
    mat.append(l)

u = cl[0]
d = cl[1]

for _ in range(T):
    temp = []
    for r in range(R):
        for c in range(C):
            if mat[r][c] != -1 and mat[r][c] > 4:
                # 확산 방향 count
                count = 0
                for dr,dc in move:
                    newR = r + dr
                    newC = c + dc

                    if 0<= newR < R and 0 <= newC < C and mat[newR][newC] != -1:
                        count += 1
                        temp.append((newR,newC,mat[r][c]//5))

                mat[r][c] -= (mat[r][c]//5)*count
    
    # 한꺼번에 확산값 적용
    for r,c,v in temp:
        mat[r][c] += v

    # shift
    for i in range(u-1,0,-1):
        mat[i][0] = mat[i-1][0]
    for i in range(d+1,R-1):
        mat[i][0] = mat[i+1][0]
    for i in range(C-1):
        mat[0][i] = mat[0][i+1]
        mat[-1][i] = mat[-1][i+1]
    for i in range(u):
        mat[i][-1] = mat[i+1][-1]
    for i in range(R-1,d,-1):
        mat[i][-1] = mat[i-1][-1]
    for i in range(C-1,0,-1):
        mat[u][i] = mat[u][i-1]
        mat[d][i] = mat[d][i-1]
    mat[u][1] = mat[d][1] = 0

# 출력
print(sum(sum(mat,[]))+2)
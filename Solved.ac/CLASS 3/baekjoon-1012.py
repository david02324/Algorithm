import sys
from collections import deque
input = sys.stdin.readline

# # bfs
# def findArea(M,N,K):
#     farm = [[False]*M for _ in range(N)]
#     for _ in range(K):
#         X,Y = map(int,input().split())
#         farm[Y][X] = True

#     areaCount = 0
#     queue = deque()
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]

#     for y in range(N):
#         for x in range(M):
#             if farm[y][x]:
#                 areaCount += 1
#                 farm[y][x] = False
#                 queue.append((x,y))
#                 while queue:
#                     coord = queue.popleft()
#                     tx = coord[0]
#                     ty = coord[1]

#                     for i in range(4):
#                         newX = tx + dx[i]
#                         newY = ty + dy[i]
#                         if 0 <= newX < M and 0 <= newY < N and farm[newY][newX]:
#                             farm[newY][newX] = False
#                             queue.append((newX,newY))
                        
#     return areaCount

# # dfs
# def findArea(M,N,K):
#     farm = [[False]*M for _ in range(N)]
#     for _ in range(K):
#         X,Y = map(int,input().split())
#         farm[Y][X] = True

#     areaCount = 0
#     stack = []

#     for y in range(N):
#         for x in range(M):
#             if farm[y][x]:
#                 areaCount += 1
#                 stack.append((x,y))
#                 while stack:
#                     tx = stack[-1][0]
#                     ty = stack[-1][1]
#                     farm[ty][tx] = False
#                     if tx < M-1 and farm[ty][tx+1]:
#                         stack.append((tx+1,ty))
#                         continue
#                     if ty < N-1 and farm[ty+1][tx]:
#                         stack.append((tx,ty+1))
#                         continue
#                     if tx > 0 and farm[ty][tx-1]:
#                         stack.append((tx-1,ty))
#                         continue
#                     if ty > 0 and farm[ty-1][tx]:
#                         stack.append((tx,ty-1))
#                         continue
#                     stack.pop()
    
#     return areaCount

for _ in range(int(input())):
    M,N,K = map(int,input().split())
    print(findArea(M,N,K))
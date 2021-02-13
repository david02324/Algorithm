# dawitblog.tistory.com
from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
# 입력받은 행렬
mat = [list(map(int,input().split())) for _ in range(n)]

# 플로이드-와샬
for k in range(n):
    for a in range(n):
        for b in range(n):
            if mat[a][k] and mat[k][b]:
                mat[a][b] = 1

print('\n'.join(' '.join(map(str,mat[i])) for i in range(n)))


# # bfs
# from sys import stdin
# from collections import deque
# input = stdin.readline

# n = int(input())
# # 입력받은 행렬
# mat = [list(map(int,input().split())) for _ in range(n)]
# # 출력할 행렬
# mat2 = []

# # 각 정점마다 수행
# for i in range(n):
#     temp = mat[i].copy()
#     visited = [False] * n
#     queue = deque([j for j in range(n) if mat[i][j]])
#     for k in queue:
#         visited[k] = True

#     # bfs
#     while queue:
#         t = queue.popleft()
#         for k in range(n):
#             if mat[t][k] and not visited[k]:
#                 temp[k] = 1
#                 visited[k] = True
#                 queue.append(k)

#     mat2.append(temp)

# # 출력
# print('\n'.join(' '.join(map(str,mat2[i])) for i in range(n)))
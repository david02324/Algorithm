# dawitblog.tistory.com
# BFS
from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
roots = [0]*(n+1)
connections = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().split())
    connections[a].append(b)
    connections[b].append(a)

queue = deque([1])
roots[1] = True
while queue:
    root = queue.popleft()
    for child in connections[root]:
        if not roots[child]:
            roots[child] = root
            queue.append(child)

print(*roots[2:],sep='\n')

# DFS
# # dawitblog.tistory.com
# from sys import stdin
# input = stdin.readline

# n = int(input())
# roots = [0]*(n+1)
# connections = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     a, b = map(int,input().split())
#     connections[a].append(b)
#     connections[b].append(a)

# stack = [1]
# roots[1] = True
# while stack:
#     root = stack[-1]
#     l = len(stack)
#     for child in connections[root]:
#         if not roots[child]:
#             roots[child] = root
#             stack.append(child)
#             break
#     if l == len(stack):
#         stack.pop()

# print(*roots[2:],sep='\n')

# OTHER
# # dawitblog.tistory.com
# from sys import stdin
# input = stdin.readline

# n = int(input())
# roots = [0]*(n+1)
# connections = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     a, b = map(int,input().split())
#     connections[a].append(b)
#     connections[b].append(a)

# stack = [1]
# roots[1] = True
# while stack:
#     root = stack.pop()
#     for child in connections[root]:
#         if not roots[child]:
#             roots[child] = root
#             stack.append(child)

# print(*roots[2:],sep='\n')
# dawitblog.tistory.com
# # DFS
# def dfs(length):
#     if length == m:
#         print(*result)
#         return
#     for temp in l:
#         if temp not in result:
#             result.append(temp)
#             dfs(length+1)
#             result.pop()

# result = []
# n,m = map(int,input().split())
# l = sorted(list(map(int,input().split())))
# dfs(0)

from itertools import permutations

result = []
n,m = map(int,input().split())
l = sorted(list(map(int,input().split())))
for case in permutations(l,m):
    print(*case)
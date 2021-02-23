# dawitblog.tistory.com
# # DFS
# def dfs(length,idx):
#     if length == m:
#         print(*result)
#         return
#     for i in range(idx,n):
#         result.append(l[i])
#         dfs(length+1,i)
#         result.pop()

# result = []
# n,m = map(int,input().split())
# l = sorted(list(map(int,input().split())))
# dfs(0,0)

# from itertools import combinations_with_replacement
# n,m = map(int,input().split())
# l = sorted(list(map(int,input().split())))
# ans = list(combinations_with_replacement(l,m))
# for result in ans:
#     print(*result)
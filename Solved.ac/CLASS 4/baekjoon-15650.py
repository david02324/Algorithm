# dawitblog.tistory.com

# # DFS
# def dfs(length,number):
#     if length == m:
#         print(*result)
#         return
#     for temp in range(number,n+1):
#         result.append(temp)
#         dfs(length+1,temp+1)
#         result.pop()

# result = []
# n,m = map(int,input().split())
# dfs(0,1)

# # 조합
# from itertools import combinations
# n,m = map(int,input().split())
# for case in combinations(range(1,n+1),m):
#   print(*case)
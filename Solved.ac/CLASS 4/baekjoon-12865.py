# dawitblog.tistory.com
from sys import stdin
input = stdin.readline

n, k = map(int,input().split())
dp = [0]*(k+1)
for _ in range(n):
    w, v = map(int,input().split())
    for j in range(k,0,-1):
        if j >= w:
            dp[j] = max(dp[j],dp[j-w]+v)

print(dp[k])
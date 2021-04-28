# dawitblog.tistory.com/146
from sys import stdin
input = stdin.readline

# 입력
n = int(input())
dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]
walls = [False]*(n*n)
# 벽 정보 입력
for r in range(n):
    l = list(map(int,input().split()))
    for c in range(n):
        if l[c] == 1:
            walls[r*n+c] = True

dp[0][1][0] = 1
for r in range(n):
    for c in range(2,n):
        if not walls[r*n+c]:
            # 가로 확인
            dp[r][c][0] += dp[r][c-1][0] + dp[r][c][0] + dp[r][c-1][2]

            if r:
                # 세로 확인
                dp[r][c][1] += dp[r-1][c][1] + dp[r-1][c][2]

                # 대각선 확인
                if not walls[r*n+c-1] and not walls[(r-1)*n+c]:
                    dp[r][c][2] += dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]
                
#출력
print(sum(dp[n-1][n-1]))
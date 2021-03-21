# dawitblog.tistory.com
# 입력
s1 = input()
s2 = input()
l1 = len(s1)
l2 = len(s2)

# dp 테이블
dp = [[0]*(l2+1) for _ in range(l1+1)]

for i in range(l1):
    for j in range(l2):
        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])

# 출력
print(dp[-1][-1])
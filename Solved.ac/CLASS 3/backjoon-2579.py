import sys
input = sys.stdin.readline

stairs = [int(input()) for _ in range(int(input()))]
if len(stairs) < 3:
    print(sum(stairs))
    exit()
dp = [stairs[0],stairs[0]+stairs[1],max(stairs[0]+stairs[2],stairs[1]+stairs[2])] + [0] * (len(stairs)-3)
for i in range(3,len(stairs)):
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i],dp[i-2]+stairs[i])

print(dp.pop())
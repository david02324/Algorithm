req = []
for _ in range(int(input())):
    req.append(int(input()))

dp = [0,1,1,1,2,2]
if max(req) > 5:
    dp += [0] * (max(req) - 5)

    for i in range(6,max(req)+1):
        dp[i] = dp[i-1] + dp[i-5]

for r in req:
    print(dp[r])
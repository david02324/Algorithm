# DP
# import sys
# input = sys.stdin.readline

# stairs = [int(input()) for _ in range(int(input()))]
# if len(stairs) < 3:
#     print(sum(stairs))
#     exit()
# dp = [stairs[0],stairs[0]+stairs[1],max(stairs[0]+stairs[2],stairs[1]+stairs[2])] + [0] * (len(stairs)-3)
# for i in range(3,len(stairs)):
#     dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i],dp[i-2]+stairs[i])

# print(dp.pop())

# ?
from sys import stdin

a,b,c = 0,0,0

n = int(stdin.readline())
l = []
p = []
for _ in range(n):
    l.append((a,b,c))
    pb = int(stdin.readline())
    d_0,d_1,d_2 = max(b,c),a+pb,b+pb
    a,b,c = d_0,d_1,d_2
    p.append((a,b,c))

print(l)
print(p)
print(max(d_2,d_1))
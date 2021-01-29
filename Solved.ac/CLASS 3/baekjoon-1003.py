# for 문을 사용
import sys
input = sys.stdin.readline

def fibo(n):
    if n < 2:
        return n
    
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    
    return b

T = int(input())
for _ in range(T):
    n = int(input())
    print(1 if not n else fibo(n-1),fibo(n))

# DP
import sys
input = sys.stdin.readline
req = [int(input()) for _ in range(int(input()))]
dp = [0,1]
for i in range(2,max(req)+1):
    dp.append(dp[i-2]+dp[i-1])
for r in req:
    if r == 0:
        print(1, 0)
        continue
    print(dp[r-1], dp[r])
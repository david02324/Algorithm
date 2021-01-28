# 풀이 dawitblog.tistory.com/73
# 브루트포싱
n = int(input())

# 제곱수이면 그냥 1 출력
if (n**0.5) % 1 == 0:
    print(1)
    exit()

# 3개로 표현할수 있는지 확인하는 변수 t
t = False
for i in range(1,int((n//2)**0.5) + 1):
    for j in range(1,int((n - i**2)**0.5) + 1):
        if i**2 + j**2 == n:
            print(2)
            exit()
        elif (n - (i**2 + j**2))**0.5 % 1 == 0:
            t = True

# 3개의 제곱수로 표현할 수 없다면 증명에 의해 4
print(3 if t else 4)

# DP 풀이. Python으로 제출시 시간 초과
from bisect import bisect_left
N = int(input())
squares = [i*i for i in range(1,int(N**0.5)+1)]
dp = [50001] * (N + 1)


for count in range(1,N+1):
    if count in squares:
        dp[count] = 1
    else:
        for i in range(bisect_left(squares,count)-1,-1,-1):
            dp[count] = min(dp[count],1+dp[count-squares[i]])
            if dp[count] = 2:
                break

print(dp[N])
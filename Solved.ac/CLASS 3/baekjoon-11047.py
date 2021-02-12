# dawitblog.tistory.com
from sys import stdin
input = stdin.readline

n, k = map(int,input().split())
coins = [0] * n
for i in range(-1,-n-1,-1):
    coin = int(input())
    if coin == k:
        print(1)
        exit()
    else:
        coins[i] = coin

coins = [coin for coin in coins if coin < k]
count, rest, i = 0, k, 0
while rest:
    need = rest // coins[i]
    count += need
    rest -= coins[i]*need
    i += 1

print(count)
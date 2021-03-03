# dawitblog.tistory.com
from sys import stdin
input = stdin.readline

n = int(input())
t = [list(map(int,input().split())) for _ in range(n)]

for h in range(n-2,-1,-1):
    for i in range(h+1):
        t[h][i] += max(t[h+1][i],t[h+1][i+1])

print(t[0][0])
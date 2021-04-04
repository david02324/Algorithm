from sys import stdin
input = stdin.readline

n,m=map(int,input().split())
l=list(map(int,input().split()))
s=[0]
for i in range(n):
    s.append(s[-1]+l[i])
for _ in range(m):
    a,b = map(int,input().split())
    print(s[b]-s[a-1])
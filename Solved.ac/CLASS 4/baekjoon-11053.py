# dawitblog.tistory.com
from sys import stdin
input = stdin.readline

n = int(input())
l = list(map(int,input().split()))
cache = [l[0]]
for i in range(1,n):
    if l[i] > cache[-1]:
        cache.append(l[i])
    else:
        j = len(cache) - 1
        while j > 0 and cache[j-1] >= l[i]:
            j -= 1
        cache[j] = l[i]

print(len(cache))
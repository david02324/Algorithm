# dawitblog.tistory.com/154
from sys import stdin
input = stdin.readline

n = int(input())
a,b,c = map(int,input().split())
current_max = [a,b,c]
current_min = [a,b,c]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    temp = tuple(current_max)
    current_max[0] = max(temp[0],temp[1]) + a
    current_max[1] = max(temp) + b
    current_max[2] = max(temp[1],temp[2]) + c

    temp = tuple(current_min)
    current_min[0] = min(temp[0],temp[1]) + a
    current_min[1] = min(temp) + b
    current_min[2] = min(temp[1],temp[2]) + c

print(max(current_max),min(current_min))
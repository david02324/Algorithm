import sys
input = sys.stdin.readline
n = int(input())
p = [list(map(int,input().split())) for _ in range(n)]
zero = 0
one = 0

def find(y,x,n):
    global zero,one
    
    temp = p[y][x]
    for ty in range(y,y+n):
        for tx in range(x,x+n):
            if temp != p[ty][tx]:
                find(y,x,n//2)
                find(y,x+n//2,n//2)
                find(y+n//2,x,n//2)
                find(y+n//2,x+n//2,n//2)
                return
    
    if temp == 0:
        zero += 1
    else:
        one += 1

find(0,0,n)
print(zero)
print(one)
from sys import stdin
input = stdin.readline

n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]
# 카운터 리스트. 각각 -1, 0, 1 인 종이의 개수와 대응
counts = [0,0,0]

dX = [0,1,2]
dY = [0,1,2]

def find(startX,startY,n):
    num = mat[startY][startX]
    if n == 1:
        counts[num+1] += 1
        return

    for y in range(startY,startY+n):
        for x in range(startX,startX+n):
            if mat[y][x] != num:
                d = n // 3
                for dy in dY:
                    for dx in dX:
                        find(startX+dx*d,startY+dy*d,d)
                return

    counts[num+1] += 1

find(0,0,n)
print(counts[0],counts[1],counts[2],sep='\n')
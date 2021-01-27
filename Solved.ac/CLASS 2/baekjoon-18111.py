# 풀이 dawitblog.tistory.com
import sys
from collections import Counter

input = sys.stdin.readline
n,m,b = map(int,input().split())
heights = []
for _ in range(n):
    heights += list(map(int,input().split()))
allBlocks = sum(heights)
heights = Counter(heights)
bestTime = 256 * 500 * 500 * 3
bestHeight = 256

for height in range(max(heights),min(heights)-1,-1):
    time = 0
    need = (height * n * m) - (allBlocks + b)
    if need <= 0:
        for h,c in heights.items():
            if h > height:
                time += (h - height) * 2 * c
            elif h < height:
                time += (h - height) * -c
        if time < bestTime:
            bestHeight = height
            bestTime = time

print(bestTime,bestHeight)
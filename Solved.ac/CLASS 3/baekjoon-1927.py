import heapq
from sys import stdin
input = stdin.readline

minHeap = []
for _ in range(int(input())):
    req = int(input())
    if req:
        heapq.heappush(minHeap,req)
    elif minHeap:
        print(heapq.heappop(minHeap))
    else:
        print(0)
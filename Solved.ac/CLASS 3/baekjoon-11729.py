import sys
import heapq
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    req = int(input())
    if req:
        heapq.heappush(heap,-req)
    elif heap:
        print(-heapq.heappop(heap))
    else:
        print(0)
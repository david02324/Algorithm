# dawitblog.tistory.com
from sys import stdin
import heapq
input = stdin.readline

plusHeap = []
minusHeap = []
for _ in range(int(input())):
    req = int(input())
    if req:
        if req > 0:
            heapq.heappush(plusHeap,req)
        else:
            heapq.heappush(minusHeap,-req)
    else:
        if not plusHeap and not minusHeap:
            print(0)
        elif not plusHeap:
            print(-heapq.heappop(minusHeap))
        elif not minusHeap:
            print(heapq.heappop(plusHeap))
        else:
            p = heapq.heappop(plusHeap)
            m = heapq.heappop(minusHeap)

            if m <= p:
                print(-m)
                heapq.heappush(plusHeap,p)
            else:
                print(p)
                heapq.heappush(minusHeap,m)
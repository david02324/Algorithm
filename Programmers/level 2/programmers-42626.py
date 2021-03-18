from heapq import heappop,heappush,heapify

def solution(scoville,k):
    heapify(scoville)

    count = 0
    while True:
        a = heappop(scoville)
        if a < k:
            if not scoville:
                return -1
            b = heappop(scoville)
            heappush(scoville,b*2+a)
            count += 1
        else:
            return count
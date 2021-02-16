# dawitblog.tistory.com
from sys import stdin
input = stdin.readline
import heapq

for _ in range(int(input())):
    maxHeap = []
    minHeap = []
    memo = [False] * 1000000
    for k in range(int(input())):
        cmd = input().split()

        if cmd[0] == 'I':
            # 두 큐에 모두 삽입
            heapq.heappush(maxHeap,(-int(cmd[1]),k))
            heapq.heappush(minHeap,(int(cmd[1]),k))
            memo[k] = True
        # 최소값을 뺄때는
        elif cmd[1] == '-1':
            # 해당 값이 최대 힙에서 뺐던 값이라면 최소 힙에서도 제거
            while minHeap and not memo[minHeap[0][1]]:
                heapq.heappop(minHeap)
            if minHeap:
                memo[minHeap[0][1]] = False
                heapq.heappop(minHeap)
            
        # 최대값을 뺄때는
        elif cmd[1] == '1':
            # 해당 값이 최소 힙에서 뺐던 값이라면 최소 힙에서도 제거
            while maxHeap and not memo[maxHeap[0][1]]:
                heapq.heappop(maxHeap)
            if maxHeap:
                memo[maxHeap[0][1]] = False
                heapq.heappop(maxHeap)

        # 마지막에 다른 힙에서 뺐던 값을 각자의 힙에서 반영
        while minHeap and not memo[minHeap[0][1]]:
                heapq.heappop(minHeap)
        while maxHeap and not memo[maxHeap[0][1]]:
                heapq.heappop(maxHeap)

    print(f'{-maxHeap[0][0]} {minHeap[0][0]}' if maxHeap and minHeap else 'EMPTY')

# 덱과 이진 검색으로 구현
# from sys import stdin
# input = stdin.readline
# import heapq

# for _ in range(int(input())):
#     maxHeap = []
#     minHeap = []
#     memo = [False] * 1000000
#     for k in range(int(input())):
#         cmd = input().split()

#         if cmd[0] == 'I':
#             # 두 큐에 모두 삽입
#             heapq.heappush(maxHeap,(-int(cmd[1]),k))
#             heapq.heappush(minHeap,(int(cmd[1]),k))
#             memo[k] = True
#         # 최소값을 뺄때는
#         elif cmd[1] == '-1':
#             # 해당 값이 최대 힙에서 뺐던 값이라면 최소 힙에서도 제거
#             while minHeap and not memo[minHeap[0][1]]:
#                 heapq.heappop(minHeap)
#             if minHeap:
#                 memo[minHeap[0][1]] = False
#                 heapq.heappop(minHeap)
            
#         # 최대값을 뺄때는
#         elif cmd[1] == '1':
#             # 해당 값이 최소 힙에서 뺐던 값이라면 최소 힙에서도 제거
#             while maxHeap and not memo[maxHeap[0][1]]:
#                 heapq.heappop(maxHeap)
#             if maxHeap:
#                 memo[maxHeap[0][1]] = False
#                 heapq.heappop(maxHeap)

#         # 마지막에 다른 힙에서 뺐던 값을 각자의 힙에서 반영
#         while minHeap and not memo[minHeap[0][1]]:
#                 heapq.heappop(minHeap)
#         while maxHeap and not memo[maxHeap[0][1]]:
#                 heapq.heappop(maxHeap)

#     print(f'{-maxHeap[0][0]} {minHeap[0][0]}' if maxHeap and minHeap else 'EMPTY')
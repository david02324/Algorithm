import sys
# import heapq
input = sys.stdin.readline

# heap = []

# for _ in range(int(input())):
#     req = int(input())
#     if req:
#         heapq.heappush(heap,-req)
#     elif heap:
#         print(-heapq.heappop(heap))
#     else:
#         print(0)

class maxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self,item):
        self.data.append(item)
        i = len(self.data) - 1

        while i > 1:
            if self.data[i] > self.data[i//2]:
                self.data[i],self.data[i//2] = self.data[i//2],self.data[i]
                i //= 2
            else:
                break
    
    def remove(self):
        if len(self.data) > 1:
            self.data[1],self.data[-1] = self.data[-1],self.data[1]
            data = self.data.pop()
            self.maxHeapify(1)
        else:
            data = 0
        return data

    def maxHeapify(self,i):
        left = i * 2
        right = i * 2 + 1
        li = []

        if left < len(self.data) and self.data[i] < self.data[left]:
            li.append(left)
        if right < len(self.data) and self.data[i] < self.data[right]:
            li.append(right)
        
        if len(li):
            change = li[0]
            if len(li) == 2:
                change = max(li)
            self.data[i],self.data[change] = self.data[change],self.data[i]
            self.maxHeapify(change)

maxheap = maxHeap()
for _ in range(int(input())):
    req = int(input())
    if req:
        maxheap.insert(req)
    else:
        print(maxheap.remove()

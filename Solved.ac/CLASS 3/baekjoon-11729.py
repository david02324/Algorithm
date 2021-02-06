# dawitblog.tistory.com
import sys
input = sys.stdin.readline

maxHeap = [0]
def append(maxHeap,n):
    maxHeap.append(n)
    i = len(maxHeap) - 1
    while i > 1:
        if maxHeap[i//2] < maxHeap[i]:
            maxHeap[i//2],maxHeap[i] = maxHeap[i],maxHeap[i//2]
            i //= 2
        else:
            break

def pop(maxHeap):
    size = len(maxHeap)
    if size == 1:
        return 0
    elif size == 2:
        return maxHeap.pop()
    
    value = maxHeap[1]
    i = size - 1
    maxHeap[1] = maxHeap.pop()
    t = 1
    while True:
        if t*2 < i and maxHeap[t*2] > maxHeap[t]:
            maxHeap[t*2],maxHeap[t] = maxHeap[t],maxHeap[t*2]
            t *= 2
        elif t*2 + 1 < i and maxHeap[t*2+1] > maxHeap[t]:
            maxHeap[t*2+1],maxHeap[t] = maxHeap[t],maxHeap[t*2+1]
            t = t*2 + 1
        else:
            break
    return value

for _ in range(int(input())):
    req = int(input())
    if req:
        append(maxHeap,req)
    else:
        print(pop(maxHeap))
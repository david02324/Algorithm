# dawitblog.tistory.com
from collections import deque

n, k = map(int,input().split())
if k <= n:
    print(n-k)
    exit()

nodes = [[i-1,i+1,2*i] for i in range(2*k)]
visited = [False] * 2 * (k+1)
queue = deque([n])
visited[n] = True
count, addedCount, temp = 1,1,0
while queue:
    addedCount -= 1
    for near in nodes[queue.popleft()]:
        if near == k:
            print(count)
            exit()
        if near <= 2*(k-1) and not visited[near]:
            visited[near] = True
            queue.append(near)
            temp += 1

    if addedCount == 0:
        addedCount = temp
        temp = 0
        count += 1
# dawitblog.tistory.com
from collections import deque

a,b = map(int,input().split())
queue = deque([(a,0)])

while queue:
    temp,count = queue.popleft()
    n = temp * 2
    m = temp * 10 + 1

    if n == b or m == b:
        print(count+2)
        exit()
    if n < b:
        queue.append((n,count+1))
    if m < b:
        queue.append((m,count+1))

print(-1)
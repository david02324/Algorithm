# dawitblog.tistory.com
from collections import deque

n,k = map(int,input().split())
if n >= k:
    print(n-k)
    exit()
limit = 2*k-n

q = deque([(n,0)])
visited = [False] * (limit+1)
visited[n] = True

while q:
    now, time = q.popleft()

    if now == k:
        print(time)
        exit()

    tel = now * 2
    while 0 < tel <= limit and not visited[tel]:
        visited[tel] = True
        q.append((tel,time))
        tel *= 2
    
    b = now - 1
    if 0 <= b <= limit and not visited[b]:
        visited[b] = True
        q.append((b,time+1))
    
    f = now + 1
    if 0 <= f <= limit and not visited[f]:
        visited[f] = True
        q.append((f,time+1))
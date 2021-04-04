from collections import deque
from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
board = [0] * 101
for _ in range(n+m):
    x,y = map(int,input().split())
    board[x] = y

q = deque([(1,0)])
visited = [False] * 101
visited[1] = True
while q:
    now, count = q.popleft()

    if now == 100:
        print(count)
        break

    for i in range(1,7):
        if now+i <= 100 and not visited[now+i]:
            visited[now+i] = True
            if not board[now+i]:
                q.append((now+i,count+1))
            else:
                q.append((board[now+i],count+1))
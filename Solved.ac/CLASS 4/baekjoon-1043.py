# dawitblog.tistory.com/149
from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int,input().split())
l = list(map(int,input().split()))
if l[0]:
    s = set(l[1:])
else:
    print(m)
    exit()

q = deque()
pl = []
# 빈 파티 수
empty = 0
for _ in range(m):
    li = input().split()
    # 파티에 아무도 오지 않는다면
    if li[0] == '0':
        empty += 1
        continue

    t = set(map(int,li[1:]))

    if not s & t:
        pl.append(t)
    else:
        q.append(t-s)

while q:
    t = q.popleft()
    temp = []
    for party in pl:
        if not party & t:
            temp.append(party)
        else:
            q.append(party-t)
    pl = temp

print(len(pl)+empty)
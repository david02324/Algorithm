# dawitblog.tistory.com
from sys import stdin
input = stdin.readline
from collections import deque

# DSLR 계산
def dslr(n):
    d1 = n // 1000
    d2 = n // 100 - d1 * 10
    d3 = n // 10 - d2 * 10 - d1 * 100
    d4 = n - d3 * 10 - d2 * 100 - d1 * 1000
    d = (2*n)%10000
    s = n-1 if n else 9999
    l = d2 * 1000 + d3 * 100 + d4 * 10 + d1
    r = d4 * 1000 + d1 * 100 + d2 * 10 + d3

    return [d,s,l,r]

for _ in range(int(input())):
    # 출발점 a, 도착점 b
    a, b = map(int,input().split())

    visited = [False] * 10000

    # 출발점의 dslr을 계산하여 저장
    queue = deque([(dslr(a),'')])
    # 방문 처리
    visited[a] = True

    while queue:
        p = queue.popleft()
        for i,way in enumerate(p[0]):
            if i == 0:
                last = 'D'
            elif i == 1:
                last = 'S'
            elif i == 2:
                last = 'L'
            else:
                last = 'R'
            # 도착점이라면
            if way == b:
                # 이제까지의 경로 출력
                print(p[1]+last)
                queue = False
                break
            elif not visited[way]:
                visited[way] = True
                queue.append((dslr(way),p[1]+last))
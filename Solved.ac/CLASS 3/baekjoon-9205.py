import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    convNum = int(input())
    home = tuple(map(int,input().split()))

    points = []
    for _ in range(convNum):
        points.append(tuple(map(int,input().split())))
    
    dest = tuple(map(int,input().split()))
    points.append(dest)

    # dfs
    stack = [home]
    visited = [home]

    happy = False
    while stack:
        now = stack[-1]
        if now == dest:
            print('happy')
            happy = True
            break
        temp = list(stack)
        for point in points:
            if point not in visited:
                distance = abs(point[0]-now[0]) + abs(point[1]-now[1])
                if distance <= 1000:
                    stack.append(point)
                    visited.append(point)
                    break
        if temp == stack:
            stack.pop()

    if not happy:
        print('sad')
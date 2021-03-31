from collections import deque

def solution(priorities, location):
    l = len(priorities)
    dq = deque(priorities)
    
    count = 1
    while True:
        m = max(dq)
        cur = dq.popleft()
        if cur == m:
            if location == 0:
                return count
            else:
                location -= 1
            count += 1
        else:
            dq.append(cur)
            location = (location - 1) % len(dq)
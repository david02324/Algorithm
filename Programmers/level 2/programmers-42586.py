from collections import deque

def solution(progresses, speeds):
    pq = deque(progresses)
    sq = deque(speeds)
    l = len(pq)
    ans = []
    
    while pq:
        for i in range(l):
            pq[i] += sq[i]
        
        count = 0
        while pq and pq[0] >= 100:
            count += 1
            pq.popleft()
            sq.popleft()
        
        l = len(pq)
        if count:
            ans.append(count)
    
    return ans
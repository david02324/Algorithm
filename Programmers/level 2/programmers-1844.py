from collections import deque

def solution(maps):
    move = [(1,0),(0,1),(-1,0),(0,-1)]
    R = len(maps)
    C = len(maps[0])
    visited = [[False]*C for _ in range(R)]
    
    visited[0][0] = True
    q = deque([(0,0,1)])
    
    while q:
        r,c,d = q.popleft()
        if (r,c) == (R-1,C-1):
            return d
        
        for dr,dc in move:
            nr = r + dr
            nc = c + dc
            
            if 0<=nr<R and 0 <=nc<C and maps[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr,nc,d+1))
                
    return -1
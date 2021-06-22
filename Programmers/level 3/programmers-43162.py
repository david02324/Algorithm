from collections import deque

def solution(n, computers):
    # 방문 확인 리스트
    visited = [False] * n
    # 네트워크 수
    network = 0

    for i in range(n):
        # 다른 네트워크에 속하지 않았다면
        if not visited[i]:
            network += 1
            
            queue = deque([computers[i]])
            
            # BFS
            while queue:
                for idx, conn in enumerate(queue.popleft()):
                    if not visited[idx] and conn:
                        visited[idx] = True
                        queue.append(computers[idx])
                    
    return network
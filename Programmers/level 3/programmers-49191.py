from collections import deque

def solution(n, results):
    INF = 2
    li = [[0 if j == i else INF for j in range(n)] for i in range(n)]
    
    for win,lose in results:
        win -= 1
        lose -= 1
        
        li[win][lose] = 1
        li[lose][win] = -1
        
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if li[j][k] == INF and li[j][i] == li[i][k] == 1:
                    li[j][k] = 1
                if li[j][k] == INF and li[j][i] == li[i][k] == -1:
                    li[j][k] = -1
    count = 0
    for player in li:
        if INF not in player:
            count += 1
    
    return count
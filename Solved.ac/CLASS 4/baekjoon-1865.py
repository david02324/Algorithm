from sys import stdin
input = stdin.readline
INF = int(1e9)

def bf():
    for i in range(1,n+1):
        for now in range(1,n+1):
            for dest, cost in nodes[now]:
                if dist[dest] > dist[now] + cost:
                    dist[dest] = dist[now] + cost
                    if i == n:
                        return True
    return False


T = int(input())
for _ in range(T):
    n,m,w = map(int,input().split())
    nodes = [[] for _ in range(n+1)]
    dist = [INF] * (n+1)

    for _ in range(m):
        a,b,t = map(int,input().split())
        nodes[a].append((b,t))
        nodes[b].append((a,t))

    for _ in range(w):
        a,b,t = map(int,input().split())
        nodes[a].append((b,-t))

    print('YES' if bf() else 'NO')
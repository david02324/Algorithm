# dawitblog.tistory.com/167
from sys import stdin
input = stdin.readline

# 입력
n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n):
    info = list(map(int,input().split()))
    a = info[0] - 1
    for i in range(1,len(info)-1,2):
        b = info[i] - 1
        c = info[i+1]

        tree[a].append((b,c))

# 거리를 담을 리스트
sum_list = []
# DFS
def dfs(now,prev,cost_list):
    # 잎새 노드이면서 시작점이 아닐때
    if len(tree[now]) == 1 and prev != -1:
        sum_list.append((sum(cost_list),now))
        return
    
    for next,cost in tree[now]:
        if next != prev:
            cost_list.append(cost)
            dfs(next,now,cost_list)
            cost_list.pop()

dfs(0,-1,[])
# 지름의 한 끝점(노드)
start = max(sum_list)[1]
sum_list = []
# 지름의 한 끝점에서 가장 먼 점(노드)까지의 거리
dfs(start,-1,[])
print(max(sum_list)[0])
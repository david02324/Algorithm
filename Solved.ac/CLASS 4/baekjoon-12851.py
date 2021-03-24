# dawitblog.tistory.com
from collections import deque
n, k = map(int,input().split())
if n >= k:
    print(n-k,1,sep='\n')
    exit()

check = [[-1,0] for _ in range(100001)]
q = deque()
q.append(n)
check[n] = [0,1]

while q:
    now = q.popleft()

    for new in (now-1,now+1,now*2):
        if 0<= new <= 100000:
            if check[new][0] == -1:
                check[new][0] = check[now][0] + 1
                check[new][1] = check[now][1]
                q.append(new)
            
            elif check[new][0] == check[now][0] + 1:
                check[new][1] += check[now][1]

print(check[k][0],check[k][1],sep='\n')
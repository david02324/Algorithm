n,m=map(int,input().split())
print(' '.join([str(k) for k in list(map(int,input().split())) if k < m]))
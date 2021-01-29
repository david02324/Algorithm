import sys
input = sys.stdin.readline

n, m = map(int,input().split())
h = [input().rstrip() for _ in range(n)]
s = [input().rstrip() for _ in range(m)]
hs = sorted(set(h) & set(s))
print(len(hs))
print('\n'.join(hs))
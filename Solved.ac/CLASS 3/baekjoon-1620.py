import sys
input = sys.stdin.readline

n, m = map(int,input().split())

pms = [''] + [input().rstrip() for i in range(n)]
pmDict = {}
for i in range(len(pms)):
    pmDict[pms[i]] = i

response = []
for _ in range(m):
    cmd = input().rstrip()
    if cmd.isdigit():
        response.append(pms[int(cmd)])
    else:
        response.append(str(pmDict[cmd]))

print('\n'.join(response))
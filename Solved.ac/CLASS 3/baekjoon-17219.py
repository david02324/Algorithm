import sys
input = sys.stdin.readline

n, m = map(int,input().split())
infoDict = {}
for _ in range(n):
    info = input().split()
    infoDict[info[0]] = info[1].rstrip()

passwords = []
for _ in range(m):
    passwords.append(infoDict[input().rstrip()])

print('\n'.join(passwords))
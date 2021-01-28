import sys
input = sys.stdin.readline

def bisect(S,number):
    left = 0
    right = len(S)-1
    while left <= right:
        mid = (left + right) // 2
        if S[mid] == number:
            return True
        elif S[mid] > number:
            right = mid - 1
        else:
            left = mid + 1
    
    return False

S = []
for _ in range(int(input())):
    cmd = input().split()
    
    if cmd[0] == 'add':
        if not bisect(S,int(cmd[1])):
            S.append(int(cmd[1]))
    elif cmd[0] == 'remove':
        if bisect(S,int(cmd[1])):
            S.remove(int(cmd[1]))
    elif cmd[0] == 'check':
        print(int(bisect(S,int(cmd[1]))))
    elif cmd[0] == 'toggle':
        if bisect(S,int(cmd[1])):
            S.remove(int(cmd[1]))
        else:
            S.append(int(cmd[1]))
    elif cmd[0] == 'all':
        S = [i for i in range(1,21)]
    elif cmd[0] == 'empty':
        S = []

    S.sort()
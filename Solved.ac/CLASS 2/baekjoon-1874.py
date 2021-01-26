import sys
input = sys.stdin.readline

n = int(input())
stack = []
log = []
count = 1
for _ in range(n):
    request = int(input())

    # 스택에 집어넣을지를 판단
    while count <= request:
        stack.append(count)
        log.append('+')
        count += 1
    
    # 스택에서 빼낼지를 판단
    if stack[-1] == request:
        stack.pop()
        log.append('-')
    else:
        print('NO')
        exit()
    
print('\n'.join(log))
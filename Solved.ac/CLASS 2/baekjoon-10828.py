import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    cmd = input().split()

    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(int(not bool(stack)))
    elif cmd[0] == 'top':
        if stack:
            print(stack[len(stack)-1])
        else:
            print(-1)
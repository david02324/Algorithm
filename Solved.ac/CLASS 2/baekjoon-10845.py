import sys
input = sys.stdin.readline

queue = []
for _ in range(int(input())):
    cmd = input().split()

    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        print(int(not bool(queue)))
    elif cmd[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)
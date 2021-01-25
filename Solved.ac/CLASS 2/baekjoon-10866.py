import sys
input = sys.stdin.readline

deque = []
for _ in range(int(input())):
    cmd = input().split()

    if cmd[0] == 'push_front':
        deque.insert(0,int(cmd[1]))
    elif cmd[0] == 'push_back':
        deque.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(deque))
    elif cmd[0] == 'empty':
        print(int(not bool(deque)))
    elif cmd[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if deque:
            print(deque[len(deque)-1])
        else:
            print(-1)
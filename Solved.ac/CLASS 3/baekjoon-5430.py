from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    cmd = input().rstrip()
    length = int(input())
    if length:
        li = list(input()[1:-2].split(','))
    else:
        _ = input()
        li = []

    Dcount = cmd.count('D')
    if Dcount > length:
        print('error')
        continue
    elif Dcount == length:
        print('[]')
        continue
    else:
        Dlist = list(map(len,cmd.split('R')))
        popLeft = sum(Dlist[0::2])
        popRight = sum(Dlist[1::2])

        if popRight:
            li = li[popLeft:-popRight]
        else:
            li = li[popLeft:]
        
        if len(Dlist)%2 == 0:
            li.reverse()
        print('['+','.join(li)+']')
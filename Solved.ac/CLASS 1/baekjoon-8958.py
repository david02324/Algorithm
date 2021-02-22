for _ in range(int(input())):
    l=input()
    stack=0
    score=0
    for r in l:
        if r=='O':
            stack+=1
            score+=stack
        else:
            stack=0

    print(score)